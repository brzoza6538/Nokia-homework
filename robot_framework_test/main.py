# print("\n\nhellon\n")

import os

# Upewnij się, że folder 'output' istnieje
os.makedirs('output', exist_ok=True)

# Ścieżka do pliku
file_path = os.path.join('output', 'output.txt')

# Zapisz tekst "why" do pliku
with open(file_path, 'w') as f:
    f.write("why")

print(f'Plik zapisany w: {file_path}')
