paths = [
        'm1.m2.m3',
        'm2.m5',
        'm4.*',
        'm4.*.k9',
        'm6.2',
        'm6.2000',
    ]

json =  {
        'm1': {
            'm2': {
                'm3': 55
            }
        },
        'm4': [False, 'bb', 'ccc'],
        'm6': ['a', 'b', 'c']
}


def redact_dict(json, paths):
    n = len(paths)
    for i in range(n):
        path = paths[i]
        level = path.split('.')
        len_level = len(level)
        try:
            value_0 = json[level[0]]
        except:
            continue
        # case 2
        if level[1] == '*':
            for i in range(len(value_0)):
                string = str(value_0[i])
                string_length = len(string)
                new_string = '*'*(string_length)
                value_0[i] = new_string
        #Case 3
        if level[1].isdigit():
            digit = int(level[1])
            if digit<len(value_0):
                variable = value_0[digit]
                var_len = len(variable)
                value_0[digit] = '*'*(var_len)

            else:
                pass

        #case 1
        key = value_0
        flag = False
        for i in range(1,len_level-1):
            try:
                if key[level[i]]:
                    key = key[level[i]]
                    flag = True
            except:
                break

        if flag == True:
            val = str(key[level[len_level-1]])
            n1 = len(val)
            key[level[len_level-1]] = '*'*n1
            
    return json
