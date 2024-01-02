def input_validation_integer(input_str):
    try:
        data=int(input(f"{input_str}"))
        return data
    except:
        print("Wrong Input Re-enter")
        return input_validation_integer(input_str)
def input_validation_index(index_set):
    data=input_validation_integer("ENTER INDEX ")
    if data not in index_set:
        print("Wrong Input Re-enter")
        return input_validation_index(index_set)
    else:
        return data
def input_validation_string(input_set,input_str):
    data=str(input(f"{input_str}"))
    b=0
    for i in data:
        if i not in input_set:
            b=1
            break
    if b==1:
        print(f"Wrong Input Re-enter use characters in ({input_set})")
        return input_validation_string(input_set,input_str)
    else:
        return data
def input_validation_length(len_):
    message=input(f"Enter Message (max char length = {len_}) ")
    if len(message)>len_:
        print("Re-enter Message length Exceeded")
        return input_validation_length(len_)
    else:
        return message