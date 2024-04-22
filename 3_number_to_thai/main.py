"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    thai_digits = {
        0: "ศูนย์",
        1: "หนึ่ง",
        2: "สอง",
        3: "สาม",
        4: "สี่",
        5: "ห้า",
        6: "หก",
        7: "เจ็ด",
        8: "แปด",
        9: "เก้า"
    }

    thai_place_values = {
        1: "",
        2: "สิบ",
        3: "ร้อย",
        4: "พัน",
        5: "หมื่น",
        6: "แสน",
        7: "ล้าน",
        8: "สิบล้าน",
    }

    def number_to_thai(self, number: int) -> str:
        if number < 0 or number > 10000000:
            return "invalid input. must be more than 0 or less than 10,000,000"

        number_str = str(number)
        thai_number = []
        
        for i, digit in enumerate(reversed(number_str)):
            place_value = i + 1
            if digit != "0":
                if digit == "1" and place_value == 2:
                    thai_number.append(thai_place_values[place_value])
                elif digit == "1" and place_value == 8:
                    thai_number.append(thai_place_values[place_value])
                else:
                    to_add = ""
                    if digit == "1" and place_value == 1 and number > 10:
                        to_add = "เอ็ด"
                    elif digit == "2" and place_value == 2:
                        to_add = "ยี่"
                    else:
                        to_add = thai_digits[int(digit)]
                    
                    if place_value != 1:
                        to_add += thai_place_values[place_value]
                    
                    thai_number.append(to_add)
            elif digit == "0" and number == 0:
                thai_number.append(thai_digits[0])
 
        thai_number.reverse()

        return "".join(thai_number)
