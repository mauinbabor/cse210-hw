file_project = open("life-expectancy.csv")

with open("life-expectancy.csv") as file_project:
    highest_year = 9999
    highest_country = ""
    highest_life_expectancy = 99999
    lowest_year = 0
    lowest_country = ""
    lowest_life_expectancy = 0
    for line in file_project:
        parts=line.split(",")
    #parts of csv
    entity = parts[0]
    code = parts[1] 
    year = int(parts[2])
    life_expectancy = float(parts[3])

choice=input('Enter the year of interest: ')
print()

if year < highest_year:
    highest_year = year
    highest_country = entity
    highest_life_expectancy = life_expectancy    
    print(f"The overall max life expectancy is: {highest_life_expectancy} from {highest_country} in {highest_year}")

if year > lowest_year:
    lowest_country = entity
    lowest_life_expectancy = life_expectancy   
    print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_country} in {lowest_year}")
print()
print("For the year" , choice , ":")
print()
sum = 0
count=0
select_year = choice
average_total = 0
if select_year == year:
    sum += life_expectancy
    count += 1
    
print(f"The average life expectancy across all countries was {average_total} ")
max_life = 9999
country = ""
min_life = 0
if year < max_life :
    max_life = life_expectancy
    country = entity
    print(f"The max life expectancy was in {country} with  {max_life} ")
if year > min_life :
    min_life = life_expectancy
    country = entity
print(f"The min life expectancy was in {country} with {min_life} ")