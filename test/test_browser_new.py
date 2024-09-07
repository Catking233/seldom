import seldom


class WebTestNew(seldom.TestCase):
    """Web search test case"""

    def test_new_browser(self):
        self.open("http://www.baidu.com")
        self.Keys(css="#kw").input("seldom").enter()
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")

        # open new browser
        browser = self.new_browser()
        browser.open("http://cn.bing.com")
        browser.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        browser.screenshots()
        self.assertInTitle("seldom")


if __name__ == '__main__':
    seldom.main(browser="edge")
