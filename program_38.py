
def u(ss):
 for i in range(len(ss)-1,-1,-1):
    print(ss[i],end="")

u("divyansh")



def reverse_string(ss):
  rev = ""
  for i in range(len(ss) - 1, -1, -1):
    rev = rev + ss[i]
  return rev


result = reverse_string("divyansh")
print(result)  # Output: hsnayyid