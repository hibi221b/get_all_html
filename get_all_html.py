import requests, os, sys

if len(sys.argv) != 1:
    print("Usage :  python all_html.py")
    sys.exit(1)


URL = input("target URL  :")
response = requests.get(URL)

#text = response.text
#binary = response.content


class get_all_html(object):

    def __init__(self):

        self.createDefaultFile()
        self.createNewFile()


    def createDefaultFile(self):

        if not os.path.exists("./all_text.html"):

            with open("all_text.html", "wb") as f:

                f.write(response.content)

            print("finished successfully")
            sys.exit(0)
    
    def createNewFile(self):

        if os.path.exists("./all_text.html"):

            newfile = input("new file name  :")

            with open(newfile, "wb") as f:
                f.write(response.content)

            print("created new file successfully")



if __name__ == '__main__':

    get_all_html()
