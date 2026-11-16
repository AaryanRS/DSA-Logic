class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.previous = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.current = HistoryNode(homepage)

    def visit(self, url):
        new_page = HistoryNode(url)

        # Throw away the old forward history
        self.current.next = None

        # Connect current <-> new page
        new_page.previous = self.current
        self.current.next = new_page

        # Move current to the new page
        self.current = new_page

    def back(self):
        if self.current.previous:
            self.current = self.current.previous

    def forward(self):
        if self.current.next:
            self.current = self.current.next

browser = BrowserHistory("google.com")

browser.visit("github.com")
browser.visit("youtube.com")
browser.visit("openai.com")

print(browser.current.url)   # openai.com

browser.back()
print(browser.current.url)   # youtube.com

browser.back()
print(browser.current.url)   # github.com

browser.forward()
print(browser.current.url)   # youtube.com

browser.back()
print(browser.current.url)

browser.visit("netflix.com")

browser.forward()
print(browser.current.url)