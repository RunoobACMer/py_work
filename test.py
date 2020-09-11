        ;初始化
        MOV R0, #00H
        MOV R1, #0DH
        MOV R2, #0BH
        MOV R3, #04H
        
LOOP:
        ;判断R2末尾是否为1           
        MOV A, R2
        AND A, #01H        
        JZ NOTADDPARTSUM
        ;是1部分积R0加R1
        MOV A, R0
        ADD A, R1
        MOV R0, A
NOTADDPARTSUM:
        ;R2右移
        MOV A, R2
        RR A
        MOV R2, A
        ;如果R0末尾为1
        MOV A, R0
        AND A, #01H
        JZ NOTSHIFTADD1
        ;补1
        MOV A, R2
        ADD A, #08H
        MOV R2, A
NOTSHIFTADD1:
        ;部分积右移
        MOV A, R0
        RR A
        MOV R0, A        
        ;判断循环条件
        MOV A, R3
        SUB A, #01H
        MOV R3, A
        
        JZ ENDD
        JMP LOOP
ENDD:
END

