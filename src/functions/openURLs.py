import webbrowser


def openURLs(urlArray):
    chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    for url in urlArray:
        webbrowser.get(chromePath).open(url, new=2)
        print("opened a new browser window!")