# import pathlib
import shutil
import time
# import zipfile
#
#
# def dir2zip(p, zp):
#     with zipfile.ZipFile(zp, 'a', zipfile.ZIP_DEFLATED) as z:
#         for f in p.rglob("*"):
#             if f.is_file():
#                 z.write(f, arcname=str(f.relative_to(p.parent)))
#
#
dirname = 'D:\\珠海档案馆\\疫情防控'
t_1 = time.perf_counter()
shutil.make_archive('D:\\lik_test\\疫情防控', 'zip', dirname)
t_2 = time.perf_counter()
print(t_2 - t_1)
# op = pathlib.Path('D:\\珠海档案馆\\疫情防控')
# np = pathlib.Path('D:\\lik_test\\疫情防控.zip')
# t_1 = time.perf_counter()
# dir2zip(op, np)
# t_2 = time.perf_counter()
# print(t_2 - t_1)


# import pathlib
import zipfile
import os


# def write_file(dir_path, out_path):
#     files = os.listdir(dir_path)
#     for file in files:
#         if os.path.isdir(os.path.join(dir_path, file)):
#             new_dir_path = os.path.join(dir_path, file)
#             if not os.path.exists(new_dir_path):
#                 os.mkdir(new_dir_path)
#             write_file(new_dir_path, out_path)
#         else:
#             file_path = os.path.join(dir_path, file)
#             file_out_path = os.path.join(out_path, "疫情防控.zip")
#             with zipfile.ZipFile(file=file_out_path, mode='a', compression=zipfile.ZIP_DEFLATED) as f:
#                 f.write(file_path)
#
#
# if __name__ == "__main__":
#     t_1 = time.perf_counter()
#     write_file('D:\\珠海档案馆\\疫情防控', 'D:\\lik_test')
#     t_2 = time.perf_counter()
#     print(t_2 - t_1)