from splinter.browser import Browser

def main():
  b = Browser()
  b.visit('https://www.baidu.com')
  print(b.title, b.url)
  b.quit()

if __name__ == '__main__':
  main
