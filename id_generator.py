def std_id(id):
    std_data= (
        ("saad", 1, "en24"),
        ("aftab", 2, "en25"),
        ("bilal", 3, "en26"),
        ("maaz", 4, "en27"),
        ("kaif", 5, "en28"),
        ("kamil", 6, "en29"),
        ("masab", 7, "en30"),
        ("amir", 8, "en31"),
        ("awez", 9, "en32"),
        ("touheed", 10, "en33")
    )
    for i in std:
        if i[1] == id:
            return i[0], i[2]
        
        
  
    return None 
    

roll_no = int(input('Enter your roll no: '))

result = std_id(roll_no)
if result:
    name,id=result
    print("Name:", name)
    print("ID:", id)
else:
    print('roll no not found ')