def project_to_distance(point_x,point_y,distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)
project_to_distance(2, 7, 4)

print(" ")

def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())

print(" ")

def f(val):
  return (-5*val**5+67*val**2-47)
  def max(val1,val2):
    if(val1>val2):
      return val1
    else:
      return val2

print(max(max(f(0),f(1)),max(f(3),f(4))))


print(" ")

def future_value(present_value, annual_rate, periods_per_year, years):
    
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value*(1+rate_per_period)**periods
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))


print(" ")


def area(length):
  return((((3)**0.5)/4)*length*length)

print(area(5))