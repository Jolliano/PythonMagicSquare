# The Importing of the Math library for some of the calculations in the Program
import math

myArray = []

print('Welcome to the Magic Square Validation program.')
filename = input("Input the name of the file that you want to validate (Ensure that you insert the .txt extension): ")

def extractNum(file):
    for line in file:
            for i in line.split():
                if i.isdigit():
                    myArray.append(int(i))

def valRange(d):
    n = int(len(d))
    if max(d) > n:
            print ('Error: At least one value is greater than the square of n.')
            return False
    else:
        dataStruc(d)

def dataStruc(d):
        n = int(len(d))
        n = math.sqrt(n)
        n = int(n)        

        d =[d[x:x + n] for x in range(0, len(d), n)]

        print ('The data from the file has been stored in a', n, 'by',n ,'matrix.\n')
        for i in d:
            print (i)
        print ('\nThe matrix is: \n', d)

        magic_square(d,n)
        
def magic_square(m,n):
        # This block of code checks the file to see if it is of the order n x n.
                for i in range(len(m)):
                   if len(m[i]) != len(m):
                       print ('This is not a square matrix. Therefore, it cannot be a magic square.')
                       return False
                       
        # This block of code checks the sum of each row to confirm their equality
                print ('\n--')
                print ('Checking the sum of the rows:\n')
                for r in m:
                    if sum(r) != sum(m[0]):
                        print ('The sum of the rows are not equal. Therefore this is not a square matrix.')
                        return False
                    else:
                        print ('The sum of the row ', r, 'is', sum(r))
                    
        # This block of code then checks for the sum of the diagonals
                print ('\n--')
                print ('Checking the sum of the diagonals:\n')
                if (sum(m[i][i] for i in range(n)))!= sum(m[0]):
                    print ('The sum of the first diagonal is different. This is not a magic square.')
                    return False
                else:
                    print ('The sum of the first diagonal is: ', sum(m[0]))

                if (sum(m[i][n-i-1] for i in range(n))) != sum(m[0]):
                    print ('The sum of the second diagonal is different. This is not a magic square.')
                    return False
                else:
                    print ('The sum of the second diagonal is: ', sum(m[0]))
                    
        # This block of code checks the sum of each column and compares them for equality with the sum of rows
                print ('\n--')
                print ('Checking the sum of the columns:\n')
                cols = [[r[c] for r in m] for c in range(len(m[0]))]
                for c in cols:
                   if sum(c) != sum(m[0]):
                       return False
                   else:
                        print ('The sum of the column ', c, 'is', sum(c))
                print ('\n--')
                print ('\nAll validations checks have been passed. The puzzle board uploaded is a magic square. \nThe magic square will be written into a new file named: Validated {}'.format(filename))

                h = open('Validated ' + filename, 'w+')
                for line in m:
                    h.write(' '.join(map(str,line))+'\n')
                h.close()

try:
    with open(filename) as f:
        extractNum(f)

        valRange(myArray)

except:
    print('File does not exist. Please try again')
    



