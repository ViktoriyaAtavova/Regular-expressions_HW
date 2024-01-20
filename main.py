from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def get_full_name(name_list):
    full_name_list = []
    for names in name_list[1:]:
        full_name = ' '.join(names[:3]).split(' ')
        full_name_list.append(full_name[:3])
    return full_name_list

def get_full_info(contacts_list):
    full_info_list = []
    contact_info_list = []
    for info in contacts_list[1:]:
        info[5] = format_number(info[5])
        contact_info_list.append(info[3:])
    for full_name, info in zip(get_full_name(contacts_list), contact_info_list):
        full_info_list.append(list(full_name + info))
    return full_info_list


def format_number(phone):
    pattern = r'\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3}\.)?\s?(\d{4})?\)?'
    sub_pattern = r'+7(\2)\3-\4-\5 \6 \7'
    changed_phone_numbers = re.sub(pattern, sub_pattern, phone)
    return changed_phone_numbers.strip()

def merge_lists(list_1, list_2):
    list_result = []
    for str1, str2 in zip(list_1, list_2):
        list_result.append(str1 or str2)
    return list_result

def delete_repeats(contacts_list) -> list:
    repeats_list = []
    single_list = []
    all_contact_info = get_full_info(contacts_list)
    for i, full_info in enumerate(all_contact_info):
        for full_inf in all_contact_info[i + 1:]:
            if full_info[:2] == full_inf[:2]:
                repeats_list.append(merge_lists(full_inf, full_info))
    for full_info in all_contact_info:
        repeat_count = 0
        for repeats in repeats_list:
            if full_info[0] == repeats [0] and full_info[1] == repeats [1]:
                repeat_count += 1
        if repeat_count == 0:
            single_list.append(full_info)
    return single_list+repeats_list




if __name__ == "__main__":
     list_without_repeats = delete_repeats(contacts_list)
     with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
         datawriter = csv.writer(f, delimiter=',')
         datawriter.writerows([contacts_list[0]]+list_without_repeats)
