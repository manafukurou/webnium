from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question

from selenium import webdriver
from selenium.webdriver.common.by import By


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('home/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #
    # # Chrome のオプションを設定する
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    #
    # # Selenium Server に接続する
    # driver = webdriver.Remote(
    #     command_executor='http://local.selenium:4444/wd/hub',
    #     desired_capabilities=options.to_capabilities(),
    #     options=options,
    # )
    # width = 1200
    # height = 900
    # driver.set_window_size(width, height)
    #
    # # Selenium 経由でブラウザを操作する
    # driver.get('https://tech.manafukurou.com')
    # print(driver.current_url)
    #
    # # 2.　例として記事一覧の 4 ページ目に移動する
    # driver.find_element(By.XPATH, '//*[@id="list"]/a[4]').click()
    # print(driver.current_url)
    #
    # # 3. 画面の幅をコンテンツの幅と合わせてスクリーンショットをとる
    # w = driver.execute_script('return document.body.scrollWidth')
    # h = driver.execute_script('return document.body.scrollHeight')
    # driver.set_window_size(w, h)
    # driver.save_screenshot('screenshot.png')

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



