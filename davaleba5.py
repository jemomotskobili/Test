# my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]

# my_list_sum=my_list[2] + my_list[8] + my_list[13]

# print(my_list_sum)



# my_list = [ 11, 3, 44, 22, 34, 445, 33, 7, 13]

# my_list_count = my_list.copy()

# my_list_count.sort()



# print(f"High {my_list_count[-1]}")
# print(f"Low {my_list_count[0]}")


# my_list = [43, '22', 12, 66, 210, ["hi"]]

# print(my_list.index(210))

# my_list[-1].append('hello')

# print(my_list)

# my_list.pop(2)

# print(my_list)

# my_list_2 = my_list.copy()
# my_list_2.clear()

# print(my_list)
# print(my_list_2)


# matrix = [[1, 2, 3], [4, 5, 6]]

# my_list = []

# for i in range(len(matrix[0])):
#     sum= 0
#     for j in range(len(matrix)):
#          sum += matrix[j][i]
#     my_list.append(sum)    

# print(my_list)    

my_list =[]

for i in range(3):
    list=[]
    for j in range(3):
        list.append(i * 3 + j + 1)
    my_list.append(list)    


print(my_list)    

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]



transposed_matrix=[]
for i in range(len(my_list)):
    transposed_matrix1=[]
    for j in range(len(my_list)):
        transposed_matrix1.append(0)
    transposed_matrix.append(transposed_matrix1)    

print(transposed_matrix)

for i in range(len(my_list)):
    for j in range(len(my_list)):
        transposed_matrix[i][j]=my_list[j][i]

print(transposed_matrix)        

 

       

        
            



