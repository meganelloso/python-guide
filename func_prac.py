#UDEMY COURSE PRAC

#Function Prac Exercise
#Warm-up
def lesser_of_two_evens(a, b):
    
    if a < b:
        bigger_num = b
        lesser_num = a
        modulo = b % a
    else:
        bigger_num = a
        lesser_num = b
        modulo = a % b

    if modulo == 0:
        return lesser_num
    else: return bigger_num

#Warm-up
def animal_crackers(text):
    text_split = text.split(" ")
    if text_split[0] == text_split[1]:
        return True
    else: 
        return False

#Warm-up
def makes_twenty(a, b):
    sum = a + b
    if sum == 20 or a == 20 or b == 20:
        return True
    else: return False

#Level 1 Prob

#1
def old_macdonald(name):
    new_name = ''
    for i in range(len(name)):
        if i == 3 or i == 0:
            new_name += name[i].capitalize()
        else:
            new_name += name[i].lower()
    return print(new_name)

old_macdonald('macdonald')

#2
def master_yoda(text):
    name_split = text.split()
    name_split.reverse()

    new_name = ' '.join(name_split)
    return print(new_name)

master_yoda("Hello World")

#3
def almost_there(n):
    num = [100, 200]
    check = 0
    for i in range(len(num)):
        less = num[i] - 10
        more = num[i] + 10

        if n > less and n < more:
            check += 1

    if check >= 1:
        return print(True)
    else:
        return print(False)

almost_there(209)

#Level 2

#1
def has_33(nums):
    for i in range(len(nums)):
        check_num = 0
        check_num = f'{nums[i]}' + f'{nums[i + 1]}'

        if check_num == '33':
            return print(True)
    return print(False)

has_33([1,3,3,1,1])

#2
def paper_doll(text):
    new_text = ''
    for i in range(len(text)):
        new_text += text[i] * 3
    return print(new_text)

paper_doll("Hello")

#3
def blackjack(a, b, c):
    my_list = []
    sum = 0
    final_sum = 0
    is_11 = False
    my_list.append(a, b, c)
    
    for i in len(my_list):
        num = int(my_list[i])
        if num <= 11 and num >= 1:
            sum += num
        
        if num == 11:
            is_11 = True
    
    if sum > 21 and is_11 == True:
        final_sum = sum - 10
    
    if final_sum > 21:
        return 'BUST'
    else: return sum
        
#4
def spy_game(nums):
    check = ''
    for i in range(len(nums)):
        if str(nums[i]) == '0' or str(nums[i]) == '7':
            check += str(nums[i])
    
    if check == '007':
        return print(True)
    else: return print(False)


spy_game([1,7,2,0,4,5,0])

#Lambda expressions + Map & filter functions 
#lambda create what are known as anonymous functions; one time use functions
#map func = dinadaanan niya lahat ng nasa list
#filter func = dapat returns true or false sa function na iccall

#legb rule format = local, enclosing function locals, global (module) and built-in