# sowmya - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 5) : 
    title,rating,ratingDescription,release_year,user_rating_size = datalist

    # print intermediate key-value pairs to standard output
  print(title,"\t",1)