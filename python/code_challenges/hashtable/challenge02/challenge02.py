# Write here the code challenge solution


def first_repeated(input):



    hashtable={}
    words_arr=input.split(' ')

    for word in words_arr:


        if word in hashtable.keys():

           hashtable[word]+=1 
           break
        
        hashtable[word]=1


    

    for word in words_arr:

       
        if hashtable[word]>1:


            return word
            break


    return 'No Repetition'






   
    


        

    


