import re
from fairies.langconv import *

def removeLineFeed(text):
    
    """去除换行 tab键"""
    k = text.replace('\r','').replace('\n','').replace('\t',' ')
    return k

def cht_2_chs(line):
    """转换繁体到简体"""
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_2_cht(sentence):
    """转换简体到繁体"""
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring    