def reverse_string(ch):
       if len(ch) <= 1:
              return ch
       
       else: 
              return reverse_string(ch[1:]) +ch[0]
       
ch = input("Any string: ")
print("Original string: ", ch)
print("Reversed string: ", reverse_string(ch))