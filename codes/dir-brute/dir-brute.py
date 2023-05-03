import sys
import requests

# python3 dir-brute.py https://www.nicepage.com wordlist.txt #

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def brute(url, wordlist):
    for word in wordlist:
        try:
            url_final = "{}/{}".format(url, word.strip())
            response = requests.get(url_final, headers=headers)
            code = response.status_code
            if code != 404:
                print("{} -- {}".format(url_final, code))
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as error:
            print(error)
            pass


if __name__ == "__main__":
    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, "r") as file:
        wordlist = file.readlines()
        brute(url, wordlist)
