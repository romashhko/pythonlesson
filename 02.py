def main(*args, **kwargs):
  result = ''
  
  for number in args:
     result += number

  print(args)
  print(kwargs["staff"])

main('п', 'р', 'и', 'в', 'і', 'т', name="Roma", age=21, staff="teacher" )