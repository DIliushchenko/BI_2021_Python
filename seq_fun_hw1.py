print('Hello, welcome to my project!')

#### fuction to define dna it's or not
def are_u_natural (sequence):
    
    ###go over all nucleotides ###
    for base in sequence:
        if base not in 'ATGCU':
            return False 
            break 
            
    if ('T' in sequence) and ('U' in sequence):
        return False
        
    return True
    #elif 'T' in sequence:
         #return('dna')
    
    #elif 'U' in sequence:
        #return('rna')
        
        
def transcribe (sequence):
    
    trans_seq = ''
    
    for base in sequence:
        if base == 'T':
            trans_seq += 'U'
        elif base == 't':
            trans_seq += 'u'
        else:
            trans_seq += base
        
    return(trans_seq)

def complement (sequence):
    
    if 'T' in sequence:
        type_nuc = 'dna'    
    elif 'U' in sequence:
        type_nuc = 'rna'
     
    compl_seq = ''
    
    for base in sequence:
        ## it's important! in dna A goes to T, but in rna A goes to T 
        if type_nuc == 'dna' and base == 'A':
            compl_seq += 'T'
        elif type_nuc == 'rna' and base == 'A':
            compl_seq += 'U'
        if type_nuc == 'dna' and base == 'a':
            compl_seq += 't'
        elif type_nuc == 'rna' and base == 'a':
            compl_seq += 'u'
        elif base == 'T':
            compl_seq += 'A'
        elif base == 't':
            compl_seq += 'a'
        elif base == 'U':
            compl_seq += 'A'
        elif base == 'u':
            compl_seq += 'a'
        elif base == 'C':
            compl_seq += 'G'
        elif base == 'c':
            compl_seq += 'g'
        elif base == 'G':
            compl_seq += 'C'
        elif base == 'g':
            compl_seq +='c'
    
    return(compl_seq)        


list_of_functions = ('transcribe','reverse','complement','reverse complement','exit')

### Let's type our commands!!!!
while True:
    
    print('Fuctions you can use: \n', str(list_of_functions))
    fun_dna = input('Enter command:')
    
    #check that user typed exicted 
    if fun_dna not in list_of_functions:
        print('Invalid function. Try Again!')
        continue
    
    elif fun_dna == 'exit':
        print('Good luck')
        break

    else:
        seq = input('Enter sequence:')
        upper_seq = seq.upper()

        # Chenk if it's dna/rna.         
        
        while are_u_natural(upper_seq) == False:
            
            print('Invalid alphabet. Try again!')          
            seq = (input('Enter sequence:'))
            upper_seq = seq.upper()
        
        ### use function which user typed
        if fun_dna == 'transcribe':

            #check if user tries to apply transcribe to rna
            if 'U' in upper_seq:
                print ('Function transcribe not for rna! Try again')
                continue
            else:
                print(transcribe(seq))

        elif fun_dna == 'reverse': 
            print(seq[::-1])
        elif fun_dna == 'complement':
            print(complement(seq))
        elif fun_dna == 'reverse complement':
            print(complement(seq[::-1]))