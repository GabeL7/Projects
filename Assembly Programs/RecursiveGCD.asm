.386                          ;use 32-bit instruction set
.model flat, stdcall          ;flat memory model, stdcall calling convention
.stack 4096                   ;allocate 4096 bytes for the stack

ExitProcess proto, dwExitCode:dword     ;declare ExitProcess function
include Irvine32.inc                    ;include Irvine32 library

;memory allocation for two inputs, gcd, and an error message
.data
prompt1 BYTE "Input first unsigned integer: ", 0 
prompt2 BYTE "Input second unsigned integer: ", 0 
errorMessage BYTE "Error - Input is not greater than zero", 0 
outputPrompt1 BYTE "Greatest common divisor is: ", 0 
outputPrompt2 BYTE "Greatest common divisor program", 0 

;uninitialized segment (.bss in nasm)
firstNum DWORD ?       ;first input number 
secondNum DWORD ?      ;second input number
gcd DWORD ?            ;greatest common divisor

.code
main proc
    mov edx, OFFSET outputPrompt2 
    call WriteString
    call Crlf ;\n

    ;prompt for the first input and store it into eax then firstNum
    mov edx, OFFSET prompt1 
    call WriteString
    call ReadInt            
    mov firstNum, eax              

    ;prompt for the second input and store it into eax then secondNum
    mov edx, OFFSET prompt2 
    call WriteString
    call ReadInt            
    mov secondNum, eax              

    ;firstNum into eax, check if firstNum > 0, and jump if firstNum <= 0 
    mov eax, firstNum              
    cmp eax, 0
    jle invalidInput        

    ;secondNum into eax, check if secondNum > 0, and jump if secondNum <= 0
    mov eax, secondNum              
    cmp eax, 0
    jle invalidInput        

    mov eax, firstNum              ;firstNum -> eax
    mov ebx, secondNum             ;secondNum -> ebx
    push eax                       ;push firstNum (first parameter)
    push ebx                       ;push secondNum (second parameter)
    call gcd_recursive             ;call gcd function
    add esp, 8                     ;clear the stack of two numbers -> (2 x 4 bytes = 2 numbers)
    mov gcd, eax                   ;eax -> gcd

    ;prompt for the output, gcd into eax, and print the result
    mov edx, OFFSET outputPrompt1 
    call WriteString
    mov eax, gcd        
    call WriteInt             
    call Crlf ;\n         
    invoke ExitProcess, 0    

;invalid input function that prints an error message
invalidInput:
    mov edx, OFFSET errorMessage 
    call WriteString
    call Crlf ;\n
    invoke ExitProcess, 1 ;exit with error code 1 
main endp

;recursive gcd(firstNum, secondNum) = gcd(secondNum, firstNum % secondNum)
;ebp + 8 = firstNum, ebp + 12 = secondNum
;source: https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/
gcd_recursive proc
    push ebp             ;base pointer
    mov ebp, esp         ;stack frame
    mov eax, [ebp+8]     ;firstNum -> eax
    mov ebx, [ebp+12]    ;secondNum -> ebx
    cmp ebx, 0           ;check if secondNum == 0 (base case)
    jne continue         ;else continue
    mov eax, [ebp+8]     ;firstNum
    pop ebp              ;base pointer
    ret                  

continue:
    mov edx, 0           ;0 -> edx
    mov eax, [ebp+8]     ;firstNum -> eax
    div ebx              ;eax = firstNum / secondNum, edx = firstNum % secondNum
    push edx             ;push firstNum % secondNum
    push ebx             ;push secondNum
    call gcd_recursive   ;recursive call
    add esp, 8           ;clear two numbers
    pop ebp              ;base pointer
    ret                  
gcd_recursive endp
end main                
