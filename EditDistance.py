
def CalcDistance(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    m=len(str1)
    n=len(str2)
    Matrix=[[x for x in range(n+1)] for x in range(m+1)]
    for i in range(len(Matrix)):
        Matrix[i][0]=i

    for i in range(1,len(Matrix)):
        for j in range(1,len(Matrix[i])):
            if(str1[i-1]==str2[j-1]):
                temp=Matrix[i-1][j-1]
            else:
                temp=Matrix[i-1][j-1]+2
            Matrix[i][j]=min(Matrix[i-1][j]+1,Matrix[i][j-1]+1,temp)
    print 'Matrix of ',str1,' and ', str2
    for row in Matrix:
        print row
    print '\n'
    return Matrix[m][n]


    
