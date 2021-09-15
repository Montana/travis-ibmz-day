# For IBM Z Day 2021 & Travis CI by Montana Mendy

def rotate(input,d): 
  
    # Star slicing the string into two parts, these parts go left and right 
    
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
  
    # Now I'm going to concatenate the two sliced parts together 
    
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst)) 
  
if __name__ == "__main__": 
    input = 'MontanaMendy'
    d=2
    rotate(input,d) 
