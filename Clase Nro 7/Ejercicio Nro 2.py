import time as t

def isWorkTime():
  time = t.localtime()
  current_time = t.strftime("%H:%M:%S", time)
  print("Current time: ", current_time)

  list = current_time.split(":")
  hour = int(list[0])

  if hour >= 19 or hour <= 8:
    print("NO ESTAMOS EN HORARIO DE TRABAJO")
  else:
    print("ESTAMOS EN HORARIO DE TRABAJO")


isWorkTime()


