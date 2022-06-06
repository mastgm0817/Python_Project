import csv
import os

from idna import IDNABidiError
from numpy import save

from post import Post


file_path = "./Blog_Project/data.csv"

post_list = []

if os.path.exists(file_path):
  print("로딩중입니다..")
  f = open(file_path, "r", newline="", encoding="utf-8-sig")
  reader = csv.reader(f)

  for data in reader:
    p = Post(int(data[0]),data[1],data[2],int(data[3]))
    post_list.append(p)
  
  f.close()

else:
  print("파일을 새로 만듭니다.")
  data = open("./Blog_Project/data.csv","w",newline="", encoding="utf-8-sig")
  data.close()
    

# 메뉴출력

def Write_post():
  title = input("제목을 입력하세요. >>>")
  content = input("내용을 입력하세요. >>>")
  post_id = post_list[-1].get_id()
  posting = Post(post_id+1, title, content, 0)
  post_list.append(posting)
  print("# 게시글을 작성되었습니다.")

def list_post():
  id_list = []
  for data in post_list:
    print(f"번호 : {data.get_id()}")
    print(f"제목 : {data.get_content()}")
    print(f"조회수 : {data.get_viewCount()}")
    print("")
    id_list.append(data.get_id())

  while True:
    print("Q) 글 번호를 선택해주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
    try:
      id = int(input(">>>"))
    except ValueError:
      print("숫자를 입력해주세요")
    else:
      if id in id_list:
        detail_post(id)
        break
      elif id == -1:
        break
      else:
        print("없는 글 번호 입니다.")

def detail_post(id):
  print("\n\n 게시글 상세 -")
  for post in post_list:
    if post.get_id() == id:
      post.add_view_count()
      print("번호 : ", post.get_id())
      print("제목 : ", post.get_title())
      print("내용 : ", post.get_content())
      print("조회수 : ", post.get_viewCount())
      target_post = post
  
  while True:
    print("Q) 수정 : 1 삭제 : 2 (메뉴로 돌아가려면 -1을 입력")
    try:
      choice = int(input(">>>"))
      if choice == 1:
        update_post(target_post)
        break
      elif choice == 2:
        delete_post(target_post)
        break
      elif choice == -1:
        break
      else:
        print("잘못 입력하셨습니다.")
    except ValueError:
      print("숫자를 입력해주세요.")

# 게시글 수정
def update_post(target_post):
    print("제목을 수정해주세요: ")
    u_title = input(">>>")
    print("내용을 수정해주세요: ")
    u_content = input(">>>")
    target_post.set_post(target_post.id, u_title, u_content, target_post.get_viewCount())
    print("게시글이 수정되었습니다. ")

#게시글 삭제
def delete_post(target_post):
    print("정말로 삭제하시겠습니까?")
    try:
      choice =  input(">>> Y/N : ")
      if choice == "Y":
        post_list.remove(target_post)
        print("게시글이 삭제 되었습니다.")
      if choice == "N":
        print("취소하였습니다.")
    except:
      print("Y or N is required") 
     
# 게시글 저장
def save_post():
  f = open(file_path, "w", encoding="utf-8", newline="")
  writer = csv.writer(f)
  for post in post_list:
    row = [post.get_id(), post.get_title(), post.get_content(), post.get_viewCount()]
    writer.writerow(row)
  f.close()
  print("# 저장이 완료되었습니다.")
  print("# 프로그램 종료")

while True:
  print("- 병연 & 원아 Blog -")
  print("- 메뉴를 선택해 주세요 -")
  print("1. 게시글 쓰기")
  print("2. 게시글 목록")
  print("3. 프로그램 종료")
  try:
      choice = int(input(">>>"))
  except:
      print("1부터 3까지만의 숫자를 입력하세요")
  else:
    if choice == 1:
      Write_post()
    elif choice == 2:
      list_post()

    elif choice == 3:
      print("프로그램을 종료합니다.")
      save_post()
      break


