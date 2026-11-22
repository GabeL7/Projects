.386
.model flat, stdcall
.stack 4096 ;4096 bytes for the stack

ExitProcess proto, dwExitCode:dword ;function prototype declaration
include Irvine32.inc ;include irvine32 library 

.data
    listOne DWORD 2, 4, 6, 8, 10, 12, 14 
    listOneEnd LABEL DWORD ;end of list one
    listTwo DWORD 1, 3, 5, 7, 9, 11, 13, 15
    listTwoEnd LABEL DWORD ;end of list two

    ;end - start of list = total number of bytes
    ;each dword is 4 bytes / 4 = number of items in the list
    sizeOne EQU (listOneEnd - listOne) / 4
    sizeTwo EQU (listTwoEnd - listTwo) / 4
    totalSize EQU sizeOne + sizeTwo ;total number of items after merging
    mergedList DWORD totalSize dup(0) ;store the merge sorted list
    
    ;prompts
    msg1 db "List One: ", 0
    msg2 db "List Two: ", 0
    msg3 db "Merged List: ", 0

.code
main proc
    mov esi, offset listOne ;esi points to the start of listone
    mov edi, offset listTwo ;edi points to the start of listtwo
    mov ebx, offset mergedList ;ebx points to the start of mergedlist

    mov ecx, sizeOne ;number of elements in listone -> ecx
    mov edx, sizeTwo ;number of elements in listtwo -> edx

;merge loop
mergeLoop:
    cmp ecx, 0 ;check if listone is empty
    je copyFromTwo ;jump to copy listtwo if empty
    cmp edx, 0 ;check if listtwo is empty
    je copyFromOne ;jump to copy listone if empty

    mov eax, [esi] ;current element from listone -> eax
    mov ebp, [edi] ;current element from listtwo -> ebp

    cmp eax, ebp ;compare each element
    jbe takeFromOne ;if listone element is less than or equal 

    mov [ebx], ebp ;else copy listtwo element into mergedlist
    add edi, 4 ;move to next item in listtwo
    dec edx ;decrement count 
    jmp advance ;move to next merge position

;put number into merged list, move to the next number, and decrease the counter
takeFromOne:
    mov [ebx], eax 
    add esi, 4
    dec ecx

;move to the next spot in the merged list, then go back and compare the next numbers
advance:
    add ebx, 4
    jmp mergeLoop

copyFromOne:
    cmp ecx, 0 ;if none left, done merging
    je doneMerge  
    mov eax, [esi] ;current element from listone -> eax
    mov [ebx], eax ;store it in mergedlist
    add esi, 4 ;move to the next number
    add ebx, 4 ;move to the next in mergedlist
    dec ecx ;decrement the listone counter 
    jmp copyFromOne ;loop until listone is done

;this does the same exact loop steps as above (same comments apply)
copyFromTwo:
    cmp edx, 0 
    je doneMerge
    mov eax, [edi]
    mov [ebx], eax
    add edi, 4
    add ebx, 4
    dec edx
    jmp copyFromTwo

;done merging and print out results
doneMerge:
    mov edx, offset msg1
    call WriteString

    mov esi, offset listOne
    mov ecx, sizeOne

;print out listone numbers
printListOne:
    mov eax, [esi]
    call WriteInt
    mov al, ' '
    call WriteChar
    add esi, 4
    loop printListOne
    call Crlf ;\n

    mov edx, offset msg2
    call WriteString

    mov esi, offset listTwo
    mov ecx, sizeTwo

;print out listtwo numbers
printListTwo:
    mov eax, [esi]
    call WriteInt
    mov al, ' '
    call WriteChar
    add esi, 4
    loop printListTwo
    call Crlf ;\n

    mov edx, offset msg3
    call WriteString

    mov esi, offset mergedList
    mov ecx, totalSize

;print merged list
printMerged:
    mov eax, [esi]
    call WriteInt
    mov al, ' '
    call WriteChar
    add esi, 4
    loop printMerged
    call Crlf

    invoke ExitProcess, 0
main endp
end main
