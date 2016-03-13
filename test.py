#!/usr/bin/python

'''
Exercise: Using any language of your choice write a script that does the following: 
Call http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=1
To go to next page of response you have to increment the page number in the above url. As long as the "more" field returns true, you have more data available.
The response is a JSON object which has a response key which is an array of more JSON objects. Each of them has a key called flags and within flags there is a key called hd.
Print out how many response objects have flags:hd set to true and how many have hd set to false.
'''
import simplejson, urllib2

def check_for_more(test_url, append, t, f):
    url = test_url + str(append)
    #print url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(req)
    response = urllib2.urlopen(req)
    data = simplejson.loads(response.read())
    if data['more'] == True:
        for x in range(0, len(data['response'])):
            d = data['response'][x]
            for i in d:
                if isinstance(d[i], dict):
                    e = d[i]
                    for i in e:
                        if i == 'hd':
                            #print e.get('hd')
                            if str(e.get('hd')) == 'True':
                                t += 1
                            elif str(e.get('hd')) == 'False':
                                f += 1

        append +=1
        check_for_more(test_url, append, t, f)


    else:
        print "The Url where more returned False : " + str(url)
        print "hd is True count: "  + str(t)
        print "hd is False count: " + str(f)

check_for_more('http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=', 1, 0,0)


