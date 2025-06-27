%include "asm_io.inc"
segment .data
	msg1 db "Entrer un nombre", 0
	msg2 db "Le nombre est : ", 0
	msg3 db "le nombre est negatif", 0
	msg4 db "le nombre est egal de zero", 0
	msg5 db "le nombre est positif", 0
	
segment .bss
	nb1 resd 1
	
segment .text
	global _asm_main

_asm_main :
	;printf("Entrer un nombre\n");
	mov eax, msg1
	call print_string
	call print_nl
	
	;scanf("%d", &nb1)
	call read_int
	mov [nb1], eax
	
	mov eax, [nb1]
	cmp eax, 0
	jl if_1
	; instruction else_if càd diffrent de zero
	je else_if_1
	; instruction else
	mov eax, msg5
	call print_string
	call print_nl
	jmp endif_1
	
if_1 :
	; instruction if_1
	mov eax, msg3
	call print_string
	call print_nl
	jmp endif_1
	
else_if_1 :
	; instruction if_1
	mov eax, msg4
	call print_string
	call print_nl
	jmp endif_1

	
endif_1 :	
	
	; printf("Le nombre est : ")
	mov eax, msg2
	call print_string
	
	;printf("%d", nb1);
	mov eax, [nb1]
	call print_int
	
	; return 0
	mov eax, 0
	ret