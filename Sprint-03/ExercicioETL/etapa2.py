total_gross_list = []
movies_count = 0

with open(r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-03\ExercicioETL\actors.csv', 'r') as file:
    next(file)
    
    for line in file:
        columns = line.strip().split(',')
        gross = columns[5]
        
        try:
            gross_float = float(gross.replace(',', ''))
            total_gross_list.append(gross_float)
            movies_count += 1
        except ValueError:
            pass

average_gross = sum(total_gross_list) / len(total_gross_list)

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-03\\ExercicioETL\\etapa-2.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f'Média de receita de bilheteria bruta dos principais filmes: {average_gross:.2f} milhões de dólares')
