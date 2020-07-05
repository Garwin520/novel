import json
import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

from django.urls import reverse

# Create your views here.

#首页
def indexPage(request,page_num):
    novel_list = Novels.objects.all().order_by('id')    #加order_by('id')防止发生无序排序
    paginator = Paginator(novel_list,10)    #分页
    page_num = int(page_num)
    if page_num > 8:
        page_num = 8
    try:
        data = paginator.page(int(page_num))
    except Exception as e:
        data = []
    num_list = [1,2,3,4,5,6,7,8]
    if page_num <= 4:
        pNum_list = num_list[page_num-1:page_num+3]
    else:
        pNum_list = num_list[4:]
    if page_num <= 1:
        last_page = 1
    else:
        last_page = page_num-1
    if page_num >= 8:
        next_page = 8
    else:
        next_page = page_num+1
    # for d in data:
    #     print(d.book_name)
    # print(len(data))
    return render(request,'index.html',{'pNum_list':pNum_list,'last_page':last_page,'next_page':next_page,
                                        'row1':data[:5],'row2':data[5:]})

#小说内容
def novelContent(request,book_id,chapter_num):
    novel = Novels.objects.filter(id=book_id)[0]
    chapter = Chapters.objects.filter(belong=book_id,chapter_num=chapter_num)[0]
    fb = open(chapter.chapter_url,'r')
    content = fb.read().split('\n')
    fb.close()
    chapter_num = int(chapter_num)
    chapter_list = Chapters.objects.filter(belong=book_id)
    chapter_total = len(chapter_list)
    if chapter_num <=1:
        last_chapter = 1
    else:
        last_chapter = chapter_num-1
    if chapter_num >= chapter_total:
        next_chapter = chapter_total
    else:
        next_chapter = chapter_num+1
    title = chapter.title
    return render(request,'content.html',{'novel':novel,'content':content,'last_chapter':last_chapter,'next_chapter':next_chapter,
                                          'title':title})

#小说章节
def novleChapters(request,book_id):
    novel = Novels.objects.filter(id=book_id)
    chapter_list = Chapters.objects.filter(belong=book_id)
    return render(request,'chapters.html',{'novel':novel[0],'chapter_list':chapter_list})

#搜索小说
def searchNovel(requests):
    if requests.method == 'POST':
        keyword = requests.POST.get('keyword')
        print(keyword)
        if keyword :
            novel = Novels.objects.filter(book_name__icontains=keyword) #包含查询
            if len(novel) > 0:
                return render(requests,'search.html',{'data':novel})
            else:
                return HttpResponse('对不起，没有查询到你要查找的小说')
        else:
            return HttpResponse('请输入关键词搜索')

DIR = "media/novels"

def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        print('没有此目录')
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list

def testT(request):
    # dir_list = get_file_list(DIR)
    # fb = open('%s/三国之凉人崛起/chapters/第一章 马家三郎.txt'%DIR,'r')
    # a = fb.read().split('\n')
    # fb.close()
    # print(a)

    # bid = 1
    # for name in dir_list:
    #     chapter_path = os.path.join(DIR,name,'chapters').replace('\\','/')
    #     chapter_list = get_file_list(chapter_path)
    #     chapter_num = 0
    #     for chapter in chapter_list:
    #         title = chapter.replace('.txt','')
    #         chapter_url = os.path.join(chapter_path,chapter).replace('\\','/')
    #         chapter_num += 1
    #         Chapters.objects.create(title=title,belong=bid,chapter_num=chapter_num,chapter_url=chapter_url)
    #     bid += 1
            # Chapters.objects.create()

    # for name in dir_list:
    #     json_path = os.path.join(DIR,name,'resume/%s.json'%name).replace('\\','/')
    #     fb = open(json_path,'r')
    #     novel_msg = json.load(fb)
    #     image = os.path.join('novels',name,'images/%s.jpg'%name).replace('\\','/')
    #     resume = novel_msg['resume']
    #     author = novel_msg['author']
    #     book_name = novel_msg['book_name']
    #     target = Novels.objects.filter(id=bid)
    #     bid += 1
    #     target.update(book_name=book_name,images=image,resume=resume,author=author)
    #     # Novels.objects.update(book_name=book_name,images=image,resume=resume,author=author)
    #     print(image)
    url = reverse('novel:index',kwargs={'page_num':1})  #关键字参数用kwargs 字典传入
    #url = reverse('novel:index', args=(1,))   #位置参数用args 元组传入
    return HttpResponse('%s'%url)