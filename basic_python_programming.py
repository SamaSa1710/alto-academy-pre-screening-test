#define function to calculate the temperature info of the week
#expect 7 float inputs (temperature of each day in the week)
def info_temperature():
    temperatures = []
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for day in range(7):
        temp = float(input("Enter the temperature for %s: " % days[day]))
        temperatures.append(temp)
    average = sum(temperatures) / len(temperatures)
    highest = max(temperatures)
    lowest = min(temperatures)
    sorted_temps = sorted(temperatures) #default: low to high
    variance = sum((temp - average) ** 2 for temp in temperatures) / len(temperatures)
    # return dictionary that stores 5 keys and values: average, high, low, sorted_temps(from lowest to highest),and variance
    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'sorted_temps': sorted_temps,
        'variance': variance
    }
#call the function
info = info_temperature()
print("Average temperature :", info['average'])
print("Highest temperature :", info['highest'])
print("Lowest temperature :", info['lowest'])
print("Temperatures sorted in ascending order:", info['sorted_temps'])
print("Variance of temperatures 1:", info['variance'])

#ขอยืนยันว่าทำด้วยตนเอง 100% มโนภัทร ชาญกล้้า