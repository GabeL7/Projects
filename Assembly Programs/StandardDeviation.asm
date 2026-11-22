.386                                    ;80386
.model flat,stdcall                     ;flat mem and stdcall
.stack 4096                             ;4 KB stack

ExitProcess proto, dwExitCode:dword     ;exitprocess
include Irvine32.inc                    ;include irvine library

;memory allocation for storage/strings/prompting
.data                                    
    scoreList SWORD -255, 255, -255, 255, -255, 255, -255, 255, -255, 255
    numScores dword ($ - scoreList) / 2                                            
    msg1 db "Mean: ", 0                   
    msg2 db "Standard Deviation: ", 0     
    msgError db "Error: Division by zero detected!", 0  
    mean dword 0                          
    sumSquaredDifferences dword 0         

;main program
.code 
main proc                                 
    cmp numScores, 0                      ;check to see if scoreList is empty and jump to error handling if so
    je handleError                        
    call calculateMean                    ;calculate mean function
    mov edx, offset msg1                  ;msg1 -> edx
    call WriteString                      
    mov eax, mean                         ;mean -> eax
    call WriteInt                         ;output mean
    call Crlf                             ;\n
    call calculateVariance                ;calculate variance function
    call sqrt                             ;square root computation
    mov edx, offset msg2                  ;msg2 -> edx
    call WriteString                      
    call WriteInt                         ;output standard deviation
    call Crlf                             ;\n
    invoke ExitProcess, 0                 ;exit(0)

handleError:                              ;division by 0 error handling
    mov edx, offset msgError              ;msgerror -> edx
    call WriteString                     
    invoke ExitProcess, 1                 ;exit(1) - error
main endp                                

;function that calculates the mean of the scores
calculateMean proc                        
    xor eax, eax                          ;xor eax to clear
    lea edi, scoreList                    ;scoreList -> edi
    mov ecx, numScores                    ;numScores -> ecx

;this function simply just sums up the scores in the scoreList
sum_loop:
    movsx edx, word ptr [edi]              ;current score -> edx, (sign-extend)
    add eax, edx                           ;score+sum
    add edi, 2                             ;next element
    loop sum_loop                          ;loop until ecx = 0
    mov ecx, numScores                     ;numScores -> ecx
    cdq                                    ;eax -> edx:eax, (sign-extend), 32 bit to 64 bit to match that pair
    idiv ecx                               ;divide edx:eax by ecx
    mov mean, eax                          ;mean -> eax
    ret                                    ;return
calculateMean endp

calculateVariance proc                     ;variance calculations
    xor eax, eax                           ;xor eax to hold sum of square differences
    lea edi, scoreList                     ;scoreList -> edi
    mov ecx, numScores                     ;numScores -> ecx
squaredDiff_loop:
    movsx edx, word ptr [edi]              ;current score -> edx, sign-extend
    sub edx, mean                          ;mean - score
    imul edx, edx                          
    add eax, edx                           ;edx+eax 
    add edi, 2                             ;next element
    loop squaredDiff_loop                  ;loop until ecx = 0
    mov sumSquaredDifferences, eax         ;sumSquaredDifferences -> eax
    mov eax, sumSquaredDifferences         ;sumSquaredDiff -> eax
    mov ecx, numScores                     ;numScores -> ecx
    cdq                                    ;eax -> edx:eax
    idiv ecx                               ;divide edx:eax by ecx, variance
    ret                                    ;return
calculateVariance endp

sqrt proc                                  ;function to compute a square root 
    mov ebx, 0                             ;ebx -> 0

;source: Newton-Raphson method which I made a guess check method which 
;simply just bounds the square root if it overshot then decrement ebx
;and if undershot it increments ebx, compares ecx,eax for validation/done
sqrt_loop:
    mov ecx, ebx                           ;ebx -> ecx
    imul ecx, ecx                          ;ecx^2
    cmp ecx, eax                           ;cmp ecx and eax to check guess
    jg sqrt_done                           ;jump if greater than if the guess is valid
    inc ebx                                ;else increment ebx
    jmp sqrt_loop                          ;loop until the guess is valid
sqrt_done:
    dec ebx                                ;decrement ebx if the guess is over the correct amount
    mov eax, ebx                           ;square root -> eax
    ret                                    ;return 
sqrt endp

end main                                   
