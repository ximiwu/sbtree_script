from DrissionPage import Chromium, ChromiumOptions
from time import sleep


def init_browser(exe_path, port = 9999):
    chromium_options = ChromiumOptions().set_browser_path(exe_path)
    chromium_options.set_local_port(port)
    return Chromium(addr_or_opts=chromium_options)

def work(browser):
    sbtree = browser.latest_tab

    chapter_container = sbtree.ele('x://*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div')

    videos = chapter_container.eles('@class=clearfix video')
    videos.insert(0, chapter_container.ele('@class=clearfix video current_play'))
    print(videos)

    for video in videos:
        video = video.ele('@class=fl cataloguediv-c')

        if len(video.eles('@class=fl time_icofinish')) != 0:
            continue
        video.click()

        while True:
            try:
                sbtree.ele('@class=speedBox').click()
                sleep(0.01)
            except Exception as e:
                break
        while True:
            try:
                sbtree.ele('@class=speedBox').hover()
                break
            except Exception as e:
                sleep(0.01)
        sbtree.ele('@class=speedBox').hover()
        sbtree.ele('@class=speedTab speedTab15').click()
        sbtree.ele('@class=videoArea').click()
        while (len(video.eles('@class=fl time_icofinish')) == 0):
            if sbtree.ele('@aria-label=弹题测验'):
                window = sbtree.ele('@aria-label=弹题测验')
                window.ele('@class=topic-item').child().click()
                window.ele('@class=el-dialog__footer').click()
                sleep(1)
                sbtree.ele('@class=videoArea').click()

