import time as t

def isWorkTime():
  time = t.localtime()
  current_time = t.strftime("%H:%M:%S", time)
  print("Current time: ", current_time)

  list = current_time.split(":")
  hour = int(list[0])
  hour = 11

  if hour >= 19 or hour < 9:
    print("NO ESTAMOS EN HORARIO DE TRABAJO")
  else:
    hours_left = 19 - hour
    print(f"ESTAMOS EN HORARIO DE TRABAJO, QUEDAN {hours_left} HORAS PARA SALIR")


isWorkTime()


