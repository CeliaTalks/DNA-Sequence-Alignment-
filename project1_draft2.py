correct_input1 = False 
#list of the possible correct characters
accepted_characters = ['A', 'T', 'C', 'G']
#checking that the input for reference gene is correct 
while correct_input1 == False:
        #enter the nucleotide sequences for gene here 
        sequence1 = input('enter your reference sequence: ')
        #convert input to capitals 
        sequence1 = sequence1.upper()
        #check that only 'A', 'T', 'C', 'G' have been entered 
        validation1 = [i in accepted_characters for i in sequence1]
        if all(validation1) == False:
                print('The reference sequence you entered is incorrect, please try again')
                correct_input1 = False
        else:
               correct_input1 = True 
correct_input2 = False
#checking that the input for test gene is correct 
while correct_input2 == False: 
        #enter the nucleotide sequences for gene here 
        sequence2 = input('enter your sequence: ')
        #convert input to capitals 
        sequence2 = sequence2.upper()
        #check that only 'A', 'T', 'C', 'G' have been entered 
        validation2 = [i in accepted_characters for i in sequence1]
        if all(validation2) == False:
                print('The sequence you entered is incorrect, please try again')
                correct_input2 = False
        else:
               correct_input2 = True 
#converting the sequences into a list 
seq1 = list(sequence1)
seq2 = list(sequence2)      
#this is a list from all of the sequences 
sequences_total = [seq1, seq2]
#find the difference in length but dont swap the order 
differenceinlength = abs(len(sequences_total[0]) - len(sequences_total[1]))
#find which sequence is longer
if differenceinlength != 0 and len(sequences_total[0]) > len(sequences_total[1]):
        print('The reference sequence is ' + str(differenceinlength) + ' nucleotides longer than the test sequence')
        deletion_test = differenceinlength
elif differenceinlength != 0 and len(sequences_total[0]) < len(sequences_total[1]):
       print('The test sequence is ' + str(differenceinlength) + ' nucleotides longer than the reference sequence')
       insertion_test = differenceinlength
elif differenceinlength == 0:
       print('The sequences are the same length')
       deletion_test = 0
       insertion_test = 0
#variable for the aligned sequences including '-'
#aligned_sequence[0] refers to seq1
#aligned_sequence[1] refers to seq2
aligned_sequence = [[],[]]
#count will measure the number of shifts 
count = 0 
#need to loop through each letter 
while len(seq1) > 0 or len(seq2) > 0:
    while len(seq1) >= 2 and len(seq2) >= 2: 
        #if bases are the same 
        if seq1[0] == seq2[0]:
                #add that term to new list 
                aligned_sequence[0].append(seq1[0])
                aligned_sequence[1].append(seq2[0])
                seq1.pop(0)
                seq2.pop(0)
        # if bases are not the same 
        elif seq1[0]!= seq2[0]:
                #check the next base to see if insertion/deletion
                #first checking if base in seq1 is the same as the next base in seq2  
                if seq1[1] == seq2[0]:
                        aligned_sequence[0].append(seq1[0])
                        aligned_sequence[1].append('-')
                        seq1.pop(0)
                #check if insertion/deletion in seq1
                elif seq1[0] == seq2[1]:
                        aligned_sequence[0].append('-')
                        aligned_sequence[1].append(seq2[0])
                        seq2.pop(0)
                #check if insertion is 2 bases long
                elif seq1[2] == seq2[0]:
                       aligned_sequence[0].append(seq1[0])
                       aligned_sequence[0].append(seq1[1])
                       aligned_sequence[1].append('-')
                       aligned_sequence[1].append('-')
                       del seq1[0:2]
                elif seq1[0] == seq2[2]:
                       aligned_sequence[1].append(seq2[0])
                       aligned_sequence[1].append(seq2[1])
                       aligned_sequence[0].append('-')
                       aligned_sequence[0].append('-')
                       del seq2[0:2]
                #check if mutation happened
                else:
                       aligned_sequence[0].append(seq1[0])
                       aligned_sequence[1].append(seq2[0].lower()) 
    if len(seq1) >= 1:
           aligned_sequence[0].append(seq1[0])
           seq1.pop(0)
    else: 
           aligned_sequence[1].append(seq2[0])
           seq2.pop(0)
#display the aligned sequence clearly 
print('reference sequence' + str(aligned_sequence[0]))
print('test sequence     ' + str(aligned_sequence[1]))



                       
       

            








            
           
