

import os

my_set = {'apple','banana','pear','pumpkin'}
my_path = ('/home/andy/Desktop/test4')

os.makedirs(my_path, exist_ok=False)

file_path = os.path.join(my_path, 'my_list.txt')

# Save the list
# with open(file_path, 'w') as f:
#     for item in my_set:  # Changed 'set' to 'my_set'
#         f.write(f"{item}\n")

print(len(my_set))