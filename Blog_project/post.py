class Post():
  """
    게시글 클래스
    param id : 게시글 아이디
    param title : 게시글 제목
    param content : 게시글 내용
    param viewCount : 게시글 조회수
  """
  def __init__(self, id, title, content, viewCount):
    self.id = id
    self.title = title
    self.content = content
    self.viewCount = viewCount
  
  def set_post(self, id, title, content, viewCount):
    self.id = id
    self.title = title
    self.content = content
    self.viewCount = viewCount

  def add_view_count(self):
    self.viewCount += 1

  def get_id(self):
    return self.id
  
  def get_title(self):
    return self.title
  
  def get_content(self):
    return self.content
  
  def get_viewCount(self):
    return self.viewCount


if __name__ == '__main__':
  post = Post(1, "테스트1", "내용1", 0)
  post.view_count()
  post.view_count()
  print(f"{post.get_id()}, {post.get_title()}, {post.get_content()}, {post.get_viewCount()}")