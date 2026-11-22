.386
.model flat,stdcall
.stack 4096

ExitProcess proto, dwExitCode:dword  
include Irvine32.inc 

;this section just contains message prompts and memory allocations for input and output (20 char + 0 end of line -> null terminator)
.data
    userInputBuffer db 21 dup(0)  
    inputString db "Input a string (20 chars max) >> ", 0  
 
    isPalindrome db "The string is a palindrome", 10, 13, 0  
    isntPalindrome db "The string is not a palindrome", 10, 13, 0
    
    reversedStringBuffer db 21 dup(0)  
    reversedString db "The reverse of the string is: ", 0  
    
    emptyStringErrorMessage db "Error - Empty String Entered", 10, 13, 0 

.code
main proc
    call Crlf ;\n
    call Crlf ;\n

    ;address of inputString -> EDX and print it
    mov edx, OFFSET inputString  
    call WriteString  

    ;address of userInputBuffer -> EDX and read input from user
    mov edx, OFFSET userInputBuffer  
    mov ecx, 20  
    call ReadString  

    ;character read from EAX -> ECX, test for 0 characters, if empty then jump to emptyInput
    mov ecx, eax  
    test ecx, ecx ;bitwise AND 0 & 0 
    jz emptyInput ;jump if zero flag (ZF = 1) (ECX == 0)

    mov ebx, ecx  ;ecx -> ebx

    ;Reverse the string, I used the two pointer approach where you just copy from end to start
    lea esi, userInputBuffer ;userInputBuffer -> ESI (LHS)
    lea edi, reversedStringBuffer ;reversedStringBuffer -> ESI (RHS)
    add esi, ecx ;ESI -> last character of string
    dec esi 
            
    ;iterate through entire string character by character
    ;print reversed string 
    ;checks character by character to see if they match from start to finish (2 pointer approach)
reverseLoop:
    mov al, [esi] ;ESI -> AL, this loads char in string to AL
    mov [edi], al ;AL -> EDI, store char position in AL
    inc edi ;increment EDI to point to the next reverseStringBuffer byte
    dec esi ;decrement ESI to point to the previous char in the string
    loop reverseLoop ;continue looping for all characters in the string
    mov byte ptr [edi], 0 ;store null terminator (0) for end of string 

    ;Print reversed string
    mov edx, OFFSET reversedString ;reversedString -> EDX
    call WriteString ;print reversedStringMessagePrompt
    mov edx, OFFSET reversedStringBuffer ;reversedStringBuffer -> EDX
    call WriteString ;prints reversedString
    call Crlf ;\n

    ;Palindrome logic 
    xor esi, esi ;reset ESI to 0
    lea edi, [ebx - 1] ;ebx - 1 -> EDI 
    shr ebx, 1 ;shift ebx bits one to the right (half it)
    jz isPalindrome_ ;jump to isPalindrome_ if the string is a palindrome

    ;this loop compares character by character until no characters remain to need to be compared using 2 pointer approach
palindromeCheckLoop:
    movzx eax, byte ptr [userInputBuffer + esi] ;address + esi -> EAX, left char
    or eax, 32 ;lowercase
    movzx edx, byte ptr [userInputBuffer + edi] ;address + esi -> EDX, right char
    or edx, 32 ;lowercase
    cmp al, dl ;compare AL lower 8 bits of EAX to DL which is the lower 8 bits of EDX, AKA -> left char cmp right char
    jne notPalindrome ;if left and right characters don't match then it isn't a palindrome so jump if not equal to notPalindrome
    ;work towards center of string (2 pointer approach)
    dec edi ;move the right pointer to the left
    inc esi ;move the left pointer to the right
    dec ebx ;decrement ebx for each check 
    jnz palindromeCheckLoop ;repeat palindromeCheckLoop if there are more characters left to compare (jump if EBX is not zero)

;if the string is a palindrome, then print out isPalindrome message
isPalindrome_:
    mov edx, OFFSET isPalindrome; isPalindrome -> EDX
    call WriteString ;print isPalindrome message
    jmp exitProgram ;jump to the exit program (unconditionally)

;if the string is not a palindrome, then print out isntPalindrome message
notPalindrome:
    mov edx, OFFSET isntPalindrome ;isntPalindrome -> EDX
    call WriteString ;print isntPalindrome message
    jmp exitProgram ;jump to the exit program (unconditionally)

;if there is no input, then print out an error message
emptyInput:
    mov edx, OFFSET emptyStringErrorMessage ;emptyStringErrorMessage -> EDX
    call WriteString ;print error message
    jmp exitProgram ;jump to exit program (unconditionally)

;system("pause");exit(0)
exitProgram:
    invoke ExitProcess, 0  ; Exit the program
main endp
end main
