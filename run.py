import sys
import time
import json
from crawler.spyder import Spyder


def main(argv):
    print str.format("Crawling {0} as requested. Give me a minute!", argv)
    spyder = Spyder(argv)
    started = time.time()

    result = spyder.run()
    print json.dumps(result, indent=4, separators=(',', ': '))

    finished = time.time() - started
    print "Crawl took " + str(finished)


if __name__ == "__main__":
    main(sys.argv[1])