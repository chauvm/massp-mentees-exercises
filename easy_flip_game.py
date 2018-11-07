
# coding: utf-8
'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to compute all possible states of the string after one valid move.
Example:
Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
'''
def generate_possible_next_moves(s):
    pass
# In[45]:


def generate_possible_next_moves(s):
    count = 0
    result =[]
    for x in range(len(s)-1):
        if s[x] == s[x+1]== "+":
            count +=1
            if x == (len(s)-1):
                new_s = s[:x]+ "--"
                result.append(new_s)
            else:
                new_s = s[:x] +"--"+ s[(x+2):]
                result.append(new_s)
      
    if count == 0:
            print([])
    
    return result   
        
        
generate_possible_next_moves("+++++++-+-+-+--++-+-+")

