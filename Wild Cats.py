wild_cats = {'Leopard': ['Panthera Pardus', 'Sub-Saharan Africa', 'Rainforests', '60-70', '30-40'],
             'Cheetah': ['Acinonyx Jubatus', 'Africa & Southwest Asia', 'Prairies & Savannas', '115-135', '40-65'],
             'Tiger': ['Panthera Tigris', 'Eastern & Southern Asia', 'Grasslands & Tropical Forests', '300-400',
                       '200-300'],
             'Jaguar': ['Panthera Onca', 'South America', 'Forests', '160-190', '30-50'],
             'Lion': ['Panthera Leo', 'Sub-Saharan Africa', 'Savannas & Grasslands', '170-250', '180-190']}

print('-' * 50)
for wild_cat, info in wild_cats.items():
    print(f'Name:{wild_cat}')
    print(f'''
Scientific Name:        {info[0]}
Regions Found:          {info[1]}
Natural Habitat:        {info[2]}
Body Length (cm):       {info[3]}
Body Weight (kg):       {info[4]}''')
    print('-' * 50)

