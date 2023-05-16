from datetime import datetime

fmt = "%a %d %b %Y %H:%M:%S %z"

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    time_diff = int(abs((dt1 - dt2).total_seconds()))

    return str(time_diff)
