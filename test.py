        ;��ʼ��
        MOV R0, #00H
        MOV R1, #0DH
        MOV R2, #0BH
        MOV R3, #04H
        
LOOP:
        ;�ж�R2ĩβ�Ƿ�Ϊ1           
        MOV A, R2
        AND A, #01H        
        JZ NOTADDPARTSUM
        ;��1���ֻ�R0��R1
        MOV A, R0
        ADD A, R1
        MOV R0, A
NOTADDPARTSUM:
        ;R2����
        MOV A, R2
        RR A
        MOV R2, A
        ;���R0ĩβΪ1
        MOV A, R0
        AND A, #01H
        JZ NOTSHIFTADD1
        ;��1
        MOV A, R2
        ADD A, #08H
        MOV R2, A
NOTSHIFTADD1:
        ;���ֻ�����
        MOV A, R0
        RR A
        MOV R0, A        
        ;�ж�ѭ������
        MOV A, R3
        SUB A, #01H
        MOV R3, A
        
        JZ ENDD
        JMP LOOP
ENDD:
END

