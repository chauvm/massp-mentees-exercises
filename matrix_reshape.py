
# coding: utf-8
'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
 r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
[3,4]]
r = 2, c = 4
Output: 
[[1,2],
[3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
'''
def matrix_reshape(nums, r, c):
    pass
# In[44]:


def matrix_reshape(nums,r,c):
    count = 0
    new_list =[]
    for x in nums:
        for j in x:
            count += 1
            new_list.append(j)
    if count == r*c:
        for i in range(count):
            if i%r==0:
                result = []
                result.append(new_list[i:i+r])
                print(result) 
    else:
        for x in nums:
            result =[]
            result += x
            print(result)
        
        
matrix_reshape([[1,2,3],
                [4,5,6],
                [7,8,9],[2,4,6],[7,5,3]],4,3)

