def palindrome(phrase):
  if len(phrase)<=1:
    return True
  if phrase[0] != phrase[-1]:
    return False
  return palindrome(phrase[1:-1])

print(palindrome("civic"))
