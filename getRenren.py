# -*- coding:utf-8 -*-
'''
Created on 2012-7-3

@author: Administrator
'''
import urllib, urllib2, cookielib,re

class LoginRenren:
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    email = ''
    password = ''
    cookie = None
    cookiefile = './cookie.dat'
    friendlist = []
    path = ''
    
    def __init__(self, email, passwd, path = 'text.txt'):
        self.email = email
        self.password = passwd
        self.path = path
        #cookie
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)
        
    def login(self):
        postdata = {
        'email': self.email,
        'password': self.password,
        'origURL': 'http://www.renren.com/home',
        'key_id': '1'
        }
        postdata = urllib.urlencode(postdata)
        #用记登录
        req = urllib2.Request(
                              url = 'http://www.renren.com/ajaxLogin/login',
                              data = postdata,
                              headers = self.header
                              )
        result = urllib2.urlopen(req).read()
        self.cookie.save(self.cookiefile)
        result = str(result)
        print result
        if "true" in result:
            print '登录成功。。。'
        else:
            print "登录失败。。。"
            exit(1)
        
        
    def getfriendlist(self):
        req = urllib2.Request(
                              url = 'http://friend.renren.com/myfriendlistx.do',
                              headers = self.header
                              )
        result = urllib2.urlopen(req).read()
        self.cookie.save(self.cookiefile)
        friend = str(re.search('friends=\[{.*}\]',result).group())
        friendId = re.findall(r'"id":(.*?),.*?,"name":"(.*?)"',friend)
        fileHandle = open(self.path, 'w')
        for f in friendId:
            self.friendlist.append(f)
            fileHandle.write(f[1].decode('unicode-escape').encode('utf-8') + '\n')
            print "%s"  % f[1].decode('unicode-escape').encode('utf-8')
     
if __name__ == '__main__':
    user = LoginRenren("XXX@qq.com","XXX")
    user.login()
    user.getfriendlist()