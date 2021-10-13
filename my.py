import random

#step 1
code_list =[]
def code_generator():
    count = 0
    while count <4:
        random_int =str(random.randint(1,8))
        if random_int not in code_list:
            code_list.append(random_int)
            count+=1
    code = ''.join(code_list)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    return code

a = code_generator()

#step 2
def get_user_input():
    count = 12
    while count>0:
        get_user_input =(input("Input 4 digit code: "))
        in_place = 0
        out_place = 0
        if len(get_user_input) != 4 or get_user_input.isdigit() == False\
        or "0" in get_user_input or "9" in get_user_input:
            print('Please enter exactly 4 digits.')

        else:
            if get_user_input == a:
                print(f'Congratulations! You are a codebreaker!\nThe code was: {a}')
                for x in a:
                    for y in get_user_input:
                        if x == y:
                            if a.index(x) == get_user_input.index(y):
                                in_place += len(x)
                            else:
                                out_place += len(x)
                print(f'Number of correct digits in correct place:     {in_place}')
                print(f'Number of correct digits not in correct place: {out_place}')
                break

            else:      
                for x in a:
                    for y in get_user_input:
                        if x == y:
                            if a.index(x) == get_user_input.index(y):
                                in_place += len(x)
                            else:
                                out_place += len(x)
                
                count -= 1
            print(f'Number of correct digits in correct place:     {in_place}')
            print(f'Number of correct digits not in correct place: {out_place}')
            print('Turns left:', count)

m = get_user_input()

# step 3





#step 4 already home