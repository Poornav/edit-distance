import EditDistance as ed
str1=raw_input("Enter the source string:")
str2=raw_input("Enter the target string:")
val=ed.CalcDistance(str1,str2)
print "Edit distance of ",str1," and ",str2," is ",val
