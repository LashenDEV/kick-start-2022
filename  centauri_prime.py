def get_ruler(kingdom):
  vowel_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  kingdom.title()
  last_char = kingdom[-1]
  if last_char in vowel_list:
      ruler = 'Alice'
  elif (last_char == 'y' or last_char == 'Y'):
      ruler = 'nobody'
  else:
      ruler = 'Bob'
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()