test_list = [1, 3, 4, 3, 6, 7]   
print ("Original list : " + str(test_list)) 
res_list = [] 
for i in range(0, len(test_list)) : 
    if test_list[i] == 3 : 
        res_list.append(i) 