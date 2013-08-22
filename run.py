import time
import json
from crawler.spyder import Spyder


s = Spyder("http://gocardless.com")


started = time.time()

result = s.run()
print json.dumps(result, indent=4, separators=(',', ': '))

finished = time.time() - started
print "Crawl took " + str(finished)