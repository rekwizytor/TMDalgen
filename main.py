#program ewolujący zadaną ilość pokoleń na podstawie początkowej populacji z pliku .traj

from functions.prep_generation import prep_generation
from functions.calculator import get_calc
from functions.load_config import load_config

#wczytanie parametrow algorytmu
config = load_config('input.txt')

n_generations = config['n_generations']
pop_filename = config['pop_filename']
pop_size = config['pop_size']
n_best = config['n_best']
n_child = config['n_child']
n_mut = config['n_mut']
struct_filename = config['struct_filename']
size = config['size']
n_atoms = config['n_atoms']
n_change = config['n_change']
atom_symbol = config['atom_symbol']
mag_moment = config['mag_moment']
label = config['label']

#ustawienie kalkulatora wykorzystywanego do obliczen
calc = get_calc(label)

#przygotowanie pierwszego pokolenia na podstawie populacji poczatkowej wczytanej z podanego pliku
prep_generation(pop_filename, pop_size, n_best, n_child, n_mut,
                struct_filename, size, n_atoms, n_change, atom_symbol,
                calc, mag_moment, label, 'pop1')

#przygotowanie kolejnych pokolen
for i in range(n_generations-1):
    prep_generation(f'sorted_pop{i+1}.traj', pop_size, n_best, n_child, n_mut,
                    struct_filename, size, n_atoms, n_change, atom_symbol,
                    calc, mag_moment, label, f'pop{i+2}')