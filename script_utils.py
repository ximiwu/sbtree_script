from DrissionPage import Chromium, ChromiumOptions
from time import sleep


def init_browser(exe_path, port = 9999):
    chromium_options = ChromiumOptions().set_browser_path(exe_path)
    chromium_options.set_local_port(port)
    return Chromium(addr_or_opts=chromium_options)

def work(browser):
    sbtree = browser.latest_tab

    chapter_container = sbtree.ele('x://*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div')
    chapters = chapter_container.children()
    for chapter in chapters:
        sections = []
        for i in chapter.children():
            if i.tag == 'div':
                sections.append(i)
        for section in sections:
            videos = section.child(2).children()
            for video in videos:
                video = video.child(2)
                if video.child(3).attr('class') == 'fl time_icofinish':
                    continue
                video.click()
                sleep(2)
                while True:
                    try:
                        sbtree.ele('@class=speedBox').click()
                        break
                    except Exception as e:
                        sleep(0.1)
                sbtree.ele('@class=speedBox').click()
                sbtree.ele('@class=speedTab speedTab15').click()
                sleep(1)
                sbtree.ele('@class=videoArea').click()
                while (video.child(3).attr('class') != 'fl time_icofinish'):
                    if sbtree.ele('@aria-label=弹题测验'):
                        window = sbtree.ele('@aria-label=弹题测验')
                        window.ele('@class=topic-item').child().click()
                        window.ele('@class=el-dialog__footer').click()
                        sleep(1)
                        sbtree.ele('@class=videoArea').click()

