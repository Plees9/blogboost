import multiprocessing
import json
import random
from services.blog_request import BlogApi
from models.chatgpt_model import ChatGptModel
from bs4 import BeautifulSoup
from models.blog_model import BlogModel
import time


def splitThreadByLimit(blog_list, chunk_size):
    result = []

    # Tách danh sách gốc thành các phần con
    for i in range(0, len(blog_list), chunk_size):
        temp = blog_list[i:i + chunk_size]
        result.append(temp)
    return result

# Hàm thực hiện công việc cho mỗi tiến trình


def worker(model: BlogModel):
    blog_model = model
    if blog_model.subTopic:
        choose_subTopic = f' and it sub topic is {random.choice(blog_model.subTopic)}'
    else:
        choose_subTopic = ''
    print(f'Blog for topic {blog_model.topic}{choose_subTopic}.')
    messages = [{"role": "system", "content": "You are a content creator."},
                {"role": "user", "content": "Write a content in form html for topic sport."},
                {"role": "assistant", "content": "<html>\n<head>\n<title>Write a title of blog</title>\n</head>\n<p> Attract of blog<p><body>body of the blog</body>\n</html>"},
                {"role": "user", "content": f"Write blog for topic {blog_model.topic}{choose_subTopic}.  Write a creative title of blog realative to the topic and subtopic."}]

    content = ChatGptModel(messages=messages).content()
    soup = BeautifulSoup(content, 'html.parser')
    BlogApi().postToBlogger(blog_model.id,
                            title=soup.title.string, body=f'{soup.body}')

def main():
    
    with open('data\\blogs_data.json', 'r') as fileInput:
        blogs_data = json.load(fileInput)

    blog_models = []
    for i in range(0, len(blogs_data)):
        blog_models.append(BlogModel.fromJson(blogs_data[i]))

    blog_chunks = splitThreadByLimit(blog_list=blog_models, chunk_size=2)

    start_time = time.time()
    for blog_chunk in blog_chunks:
        # Danh sách tiến trình
        processes = []

        # Tạo và khởi động các tiến trình
        for blog_model in blog_chunk:
            p = multiprocessing.Process(target=worker, args=(blog_model,))
            processes.append(p)
            p.start()

        # Chờ cho tất cả các tiến trình hoàn thành
        for p in processes:
            p.join()
    end_time = time.time()
    elapsed_time = (end_time - start_time)/60
    print("Kết thúc trong: ", elapsed_time)

if __name__ == "__main__":
    main()

