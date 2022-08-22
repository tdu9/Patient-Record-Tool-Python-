def print_queue(*a_list, **a_dict):
    for person in a_list:
        for patient, info in a_dict.items():
            if person == patient:
                print(person + ':')
                for key, value in info.items():
                    print(key + ' = ' + str(value))
                print()

queue_list = ['Nelson', 'Tiffany', 'Raymond', 'Michelle', 'Polly']
patient_dict = {'Tiffany': {'age': 15, 'weight': 100},
                'Raymond': {'age': 23, 'weight': 165},
                'Sabrina': {'age': 20, 'weight': 120},
                'Michelle': {'age': 24, 'weight': 132},
                }
print('These waiting people are on the record.')
print_queue(*queue_list, **patient_dict)


