        ;��ʼ��
        MOV R0, #00H
        MOV R1, #03H
        MOV R2, #-4H
        MOV R3, #04H
        
        TEST R1, #80H
JZ NEXT1
        ADD R0, #01H
        SUB R1, #01H
        GETNOT R1
        
NEXT1:        
        TEST R2, #80H
JZ NEXT2
        ADD R0, #01H
        SUB R2, #01H
        GETNOT R2
NEXT2:
        MOV A, #00H
        MOV 0F1H, A
        MOV A, R0
        AND A, #01H
        MOV 0F1H, A
        MOV R0, #00H

        
LOOP:
        ;���R2���λ�Ƿ�Ϊ1
        MOV A, R2
        AND A, #01H        
        JZ NOTADDPARTSUM
        ;����1��R0��R1  
        MOV A, R0
        ADD A, R1
        MOV R0, A
NOTADDPARTSUM:
        ;R2����
        MOV A, R2
        RR A
        MOV R2, A
        ;���R0���λ�Ƿ�Ϊ1
        MOV A, R0
        AND A, #01H
        JZ NOTSHIFTADD1
        ;����1��R2���λ��1
        MOV A, R2
        ADD A, #08H
        MOV R2, A
NOTSHIFTADD1:
        ;R0����
        MOV A, R0
        RR A
        MOV R0, A        
        ;R3�Լ�һ���ж�ѭ��
        MOV A, R3
        SUB A, #01H
        MOV R3, A
        
        JZ ENDD
        JMP LOOP
ENDD:
        MOV A, 0FH
        MOV R3, A
        END
