# Write here the code challenge solution
def validate_Parentheses(s):
        '''
        validating the parentheses inside the give string   
        params: string
        return : True if the parentheses are valid, and False if not . 
        
        '''
        open_char=['(', '{', '[' ] 
        close_char=[')','}',']']
        char_pairs=['()', '{}', '[]' ]

        char_open_stack=[]
       
   
        for i in s:

            if i in open_char:

                char_open_stack.append(i)
             

            elif len(char_open_stack):
                
                if char_open_stack[-1]+i in char_pairs:
                    char_open_stack.pop() 

                elif  i in close_char:
                    return False  
                           

            else :
                return False 
                                           
        if len(char_open_stack):
            return False

        else:
            return True

             
       
