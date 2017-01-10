# -*- coding: cp1251 -*-
import re

slog = open('C:\\Users\ShaginDL\Downloads\Лог толкит.txt', 'r', encoding='utf-8').read()
slog = ''.join(re.findall(' \w\w', slog)).replace(' ', '') # оставляем только ASCII hex
slog = ''.join(re.findall('570103.*57', slog))  # 
#slog 

print(slog)
