def test_cli(page):
    page.goto("https://www.youtube.com/")


# playwright install webkit                                    - install browser
# playwright codegen youtube.com
# playwright codegen youtube.com --save-storage=auth.json      - save cookies into auth.json 
# playwright open --load-starage=auth.json youtube.com
# playwright wk youtube.com                                    - open youtube.com with webkit
# playwright open --device="iPhone 11 Pro" youtube.com         - open youtube.com on iPhone 11
#                 --viewport_size=800,600 youtube.com          - open youtube.com in 800,600 size
# playwright pdf youtube.com name_of_new_file.pdf              - kreate pdf 
# 