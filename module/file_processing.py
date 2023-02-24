import os

#read_file_names_list (str,str)-> str_lst
#("入力の場所(フォルダまでのパス)")->"入力の場所"にあるファイル名(拡張子は除く)を入れたstring型のlistを返す
#
#"入力の場所"はあるフォルダへのパス.
#フォルダの中にあるファイルの名前を読み込む.
#ファイルの名前をリストに入れていく.
#ファイルの名前を入れたリストを出力として返す.
#
#例
#("/file" , '.pdf')->["folder_1","folder_2","folder_3"]
#
# read_file_names_list(input_path)
#
#param string input_path 読み込みファイルが存在するフォルダパス
#param string file_target 読み込みたいファイルの拡張子(1つのみ)
#
#return string[] 分割されたファイル名のリスト

def read_file_names_list(input_path, ext, f):
  return([f(fn) for fn in os.listdir(input_path) if (os.path.isfile(os.path.join(input_path, fn)) & (os.path.splitext(fn)[1] == ext))])
  
#txtファイルを読み込んでlistで出力する.
#read_file_to_list(str)-> list
#("ファイルAのパス")->"ファイルA"を読み込んでlistを出力する．
#
#例
#list.txtの中身
#'apple'
#'banana'
#
#('./list/txt')->['apple', 'banana']
#
# read_file_to_list(input_file_path)
#
#param string input_file_path 読み込みたいファイルのpath
#
#return list listが出力される
#            改行の'\n'は除いている.


def read_file_to_list(file_path):
  with open(file_path) as f:
    list_strip = [s.strip() for s in f.readlines()]
  return(list_strip)
        

def write_file_from_list(file_path, list):
  with open(file_path, mode='w') as f:
    for s in list:
      f.write(s + "\n")
