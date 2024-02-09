'''
������� log_for()
���-���� � ��� ��������� ����, � ������� ������������� ������������ ������ ���������� � ������ ������� ��� ���������. �������� ���-����� �������� �����, ������ � ������ ���� ������ ����� �������, ��� ��� ���-����� ����� ��������� ������ ������:

2022-01-01 INFO: User logged in
2022-01-01 ERROR: Invalid input data
2022-01-01 WARNING: File not found
2022-01-02 INFO: User logged out
2022-01-03 INFO: User registered
�� ���� ������ ������ ���-����� ��������� ��������� �������, ������� ��������������� ����� � ������� YYYY-MM-DD, ����� � ������� ���������.

���������� ������� log_for(), ������� ��������� ��� ��������� � ��������� �������:

logfile � ��� ���-�����
date_str � ��������� ���� � ������� YYYY-MM-DD
������� ������ ��������� ��������� ���� � ������:

log_for_<date_str>.txt
� ���������� � ���� ��� ������� �� ����� logfile, ������� ��������� � ���� date_str. ������� ������ ������������ ��� �������� ����, � ����� ������������� � ����� �������� �������.

���������� 1. ��� �����, ������������� � �������, ��� �������� ����������.

���������� 2. ��� �������� ����� ����������� ����� �������� ��������� UTF-8.

���������� 3. � ����������� ������� ������ ���������, ���������� ������ ����������� ������� log_for(), �� �� ���, ���������� ��.
'''

def log_for (logfile :str, date_str :str):
    log_file_name = f'log_for_{date_str}.txt'
    with open(logfile,'r',encoding = 'utf-8') as raw:
        for line in raw.readlines():
            fil,txt = line.split(' ',maxsplit=1)
            if fil == date_str:       
                with open (log_file_name, 'a', encoding ='utf-8') as raw:
                    raw.write(txt)
                    
with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())                    
    
 