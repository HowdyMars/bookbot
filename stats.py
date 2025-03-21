#! /usr/bin/env python3

def get_word_count(txt):
    txt = txt.split()
    count = len(txt)
    return count

def get_char_count(txt):
    txt = txt.lower()
    char_dict = {}
    for char in txt:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def gen_report(char_dict):
    sorted_list = []
    for char in char_dict:
        dict = {"char": char, "count": char_dict[char]}
        sorted_list.append(dict)
    sorted_list.sort(reverse=True, key=lambda dict: dict["count"])
    return sorted_list
