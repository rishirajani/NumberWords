hundred_one_dict = {0:'',1:"one",2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
ten_dict = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

def hundreds(n):
    """
    hundreds(n) function accepts an integer n between 0 and 100 and returns its word representation.
    Input : int 0 <= n <= 100
    Ouput : string
    
    """
    num = str(n)
    i = 1
    name =''
    while i <= len(num):
        if 10 <= int(num[-2:]) <= 19 and i == 1:
            name = ' ' + ten_dict[int(num[-2:])] + name
            i = 2
            if len(num) > 2:
                name = ' and' + name
        elif i == 1:
            name = ' ' + hundred_one_dict[int(num[-i])] + name
            if len(num) > 2 and 1 <= int(num[-2:]) <= 9:
                name = ' and' + name
        elif i == 2:
            if int(num[-i]) != 0:
                name = ' ' + ten_dict[int(num[-i])] + name
                if len(num) > 2:
                    name = ' and' + name
        elif i == 3 and int(num[-i]) != 0:
            name = hundred_one_dict[int(num[-i])] + ' hundred' + name
        i+=1
    return name.strip().capitalize()
    
def grouping_func(num,formatting='universal'):
    """
    grouping_func(num,formatting) functions accepts a number between 0 and 999,999,999 as a string and outputs its word representation.
    formatting is the parameter that tells the function which to formatting to choose, i.e., universal or indian. Default is universal
    Input : string
    Output : string
    
    """
    name = ''
    if num == '0':
        name = 'zero'
        return name.capitalize()
    if len(num) > 9:
        return "Number is too long"
    elif formatting == 'universal':
        if 6 < len(num) <= 9:
            if int(num[:-6]) > 0:
                name += hundreds(int(num[:-6])) + ' million, '
        if len(num) > 3:
            if int(num[-6:-3]) >0:
                name += hundreds(int(num[-6:-3])) +' thousand, '
        name += hundreds(int(num[-3:]))
        return name.capitalize().strip().strip(',')
    elif formatting == 'indian':
        if 7 < len(num) <= 9:
            if int(num[:-7]) > 0:
                name += hundreds(int(num[:-7])) + ' crore, '
        if 5 < len(num):
            if int(num[-7:-5]) > 0:
                name += hundreds(int(num[-7:-5])) + ' lakh, '
        if len(num) > 3:
            if int(num[-5:-3]) >0:
                name += hundreds(int(num[-6:-3])) +' thousand, '
        name += hundreds(int(num[-3:]))
        return name.capitalize().strip().strip(',')
