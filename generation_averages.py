import sys
import json

labels = {
    'bat_wap': 'Battery',
    'cg_wap': 'Coal',
    'cog_wap': 'Cogen',
    'gas_wap': 'Gas',
    'geo_wap': 'Geothermal',
    'hyd_wap': 'Hydro',
    'liq_wap': 'Diesel/Oil',
    'win_wap': 'Wind'
}

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

if len(sys.argv) != 4:
    print('Usage: python3 generation_averages.py <filename> <month> <year>')
    sys.exit(1)

filename = sys.argv[1]
month = int(sys.argv[2])
year = int(sys.argv[3])

try:
    content = read_file(filename)
except FileNotFoundError:
    print(f'Error: File {filename} not found')
    sys.exit(1)

# Load the data as a Python object
parsed_data = json.loads(content)
items = parsed_data['items']

# Maps to store the generation types
gen_waps = {}
gen_counts = {}

# Iterate through the items in the data
for item in items:
    trading_date = item['trading_date']
    trading_month = int(trading_date[5:7])
    trading_year = int(trading_date[:4])
    
    if trading_month == month and trading_year == year:
        for generation_type in item['generation_type']:
            for field in generation_type:
                if 'wap' in field:
                    if field in gen_waps:
                        gen_waps[field] += generation_type[field]
                    else:
                        gen_waps[field] = generation_type[field]
                    
                    if field in gen_counts:
                        gen_counts[field] += 1
                    else:
                        gen_counts[field] = 1

for wap in gen_waps:
    wap_average = gen_waps[wap] / gen_counts[wap] if gen_counts[wap] > 0 else 0
    print(f'{month}/{year} Average for {labels[wap]}: {wap_average:.2f}')