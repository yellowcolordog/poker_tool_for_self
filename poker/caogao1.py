from poker import *
from range import *
from card_type import *
#
file_path1 = r'E:\扑克研究\自制扑克软件\solver_range\bluffTheSpot\bb'
file_path2 = r'E:\扑克研究\自制扑克软件\solver_range\bluffTheSpot\Def'

# bbrg1 = solver_file_to_rg('E:\扑克研究\自制扑克软件\solver_range\BB-all range.txt')

# print_rp(rg_to_rp(new_bbrg))
# print_rp(rg_to_rp(bbrg2))
#
# for name in os.listdir(file_path1):
#     bbrg2 = solver_file_to_rg(os.path.join(file_path1,name))
#     new_rg = rg1_sub_rg2(bbrg1,bbrg2)
#     solver_lr = rg_to_solver_rl(new_rg)
#     new_name = 'Def'+name
#     save_solver_rl(new_name,solver_lr,filename=file_path2)

btnrg1 = solver_file_to_rg(r'E:\扑克研究\自制扑克软件\solver_use_range\Btndef原始.txt')
btnrg2 = solver_file_to_rg(r'E:\扑克研究\自制扑克软件\solver_range\bluffTheSpot\3B\3BUTG.txt')

file_path2 = r'E:\扑克研究\自制扑克软件\solver_range\temp_range'


new_rg = rg1_sub_rg2(btnrg1,btnrg2)
solver_lr = rg_to_solver_rl(new_rg)
new_name = 'Defbtn'
rp = rg_to_rp(new_rg)
print_rp(rp)

if input() == '1':
    save_solver_rl('Btndef3.txt',solver_lr)