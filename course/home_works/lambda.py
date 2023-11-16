import csv
with open('2019.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    av_par = csv_reader.fieldnames[3:]
    print(f'Parameters are: ')
    for par in av_par:
        print(par)
    sel_par = input(f'Please enter parameter: ')
    top_count = int(input('Please enter number of countries: '))
    country_list = sorted(csv_reader, key=lambda x: float(x[sel_par]), reverse=True)
    if top_count <= len(country_list):
        print(f'Top {top_count} countries by {sel_par}:')
        for i in range(top_count):
            country = country_list[i]
            print(f'{i + 1}.{country["Country or region"]}({sel_par}:{country[sel_par]})')
    else:
        print(f'The number of countries is wrong!')


