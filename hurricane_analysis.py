# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def new_damages(damages):
  updated_damages = []
  conversion = {"M": 1000000,
              "B": 1000000000}
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    elif damage[-1] in conversion.keys():
      new_value = float(damage[:-1]) * conversion[damage[-1]]
      updated_damages.append(new_value)
  return updated_damages
updated_damages = new_damages(damages)

# test function by updating damages

# 2 
# Create a Table
def dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = dict()
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes
hurricanes = dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# Create and view the hurricanes dictionary

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def hur_year_dictionary(hurricanes):
  hur_by_year= dict()
  for name in hurricanes:
    current_year = hurricanes[name]['Year']
    current_hur = hurricanes[name]
    if current_year not in hur_by_year:
        hur_by_year[current_year] = [current_hur]
    else:
        hur_by_year[current_year].append(current_hur)
  return hur_by_year
hur_by_year = hur_year_dictionary(hurricanes)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def hur_counting_dictionary(hurricanes):
  hur_count = dict()
  for name in hurricanes: 
    area_affected = hurricanes[name]['Areas Affected']
    for area in area_affected:
      if area not in hur_count:
        hur_count[area] = 1 
      else:
        hur_count[area] += 1
  return hur_count
hur_count = hur_counting_dictionary(hurricanes)
#print(hur_count)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def max_hur_count(hurricanes):
  max_area = ''
  max_area_count = 0
  for area in hur_count:
    if hur_count[area] > max_area_count:
      max_area = area
      max_area_count = hur_count[area]
  return max_area, max_area_count 
max_area, max_area_count = max_hur_count(hurricanes)
# 6
# Calculating the Deadliest Hurricane
def max_hur_deaths(hurricanes):
  max_mortality_hur = ''
  max_mortality = 0
  for name in hurricanes:
    if hurricanes[name]['Death'] > max_mortality:
      max_mortality = name
      max_mortality_count = hurricanes[name]['Death']
  return 
# find highest mortality hurricane and the number of deaths


# 7
# Rating Hurricanes by Mortality
def mortality_def(hurricanes):
  hur_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]} 
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for name in hurricanes:
    hur_mort = hurricanes[name]['Deaths']
    if hur_mort == mortality_scale[0]:
      hur_mortality[0].append(hurricanes[name])
    elif hur_mort > mortality_scale[0] and hur_mort <= mortality_scale[1]:
      hur_mortality[1].append(hurricanes[name])
    elif hur_mort > mortality_scale[1] and hur_mort <= mortality_scale[2]:
      hur_mortality[2].append(hurricanes[name])
    elif hur_mort > mortality_scale[2] and hur_mort <= mortality_scale[3]:
      hur_mortality[3].append(hurricanes[name])
    elif hur_mort > mortality_scale[3] and hur_mort <= mortality_scale[4]:
      hur_mortality[4].append(hurricanes[name])
    elif hur_mort > mortality_scale[4]:
      hur_mortality[5].append(hurricanes[name])
  return hur_mortality
hur_mortality = mortality_def(hurricanes)
#print(hur_mortality)
# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def max_hur_damage(hurricanes):
  max_damage_hur = ''
  max_damage = 0
  for name in hurricanes:
    if hurricanes[name]['Damage'] == "Damages not recorded":
      pass
    elif hurricanes[name]['Damage'] > max_damage:
      max_damage_hur = name
      max_damage = hurricanes[name]['Damage']
  return max_damage_hur, max_damage
max_damage_hur, max_damage = max_hur_damage(hurricanes)

# 9
# Rating Hurricanes by Damage
def damages_def(hurricanes):
  hur_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for name in hurricanes:
    damage_hur = hurricanes[name]['Damage']
    if damage_hur == 'Damages not recorded':
      hur_damage[0].append(hurricanes[name])
    elif damage_hur > damage_scale[0] and damage_hur <= damage_scale[1]:
      hur_damage[1].append(hurricanes[name])
    elif damage_hur > damage_scale[1] and damage_hur <= damage_scale[2]:
      hur_damage[2].append(hurricanes[name])
    elif damage_hur > damage_scale[2] and damage_hur <= damage_scale[3]:
      hur_damage[3].append(hurricanes[name])
    elif damage_hur > damage_scale[3] and damage_hur <= damage_scale[4]:
      hur_damage[4].append(hurricanes[name])
    elif damage_hur > damage_scale[4]:
      hur_damage[5].append(hurricanes[name])
  return hur_damage
hur_damage = damages_def(hurricanes)
