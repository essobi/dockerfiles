# The MIT License (MIT)  
#  
# Copyright (c) 2016 Extesla, LLC.  
#  
# Permission is hereby granted, free of charge, to any person obtaining  
# a copy of this software and associated documentation files (the  
# "Software"), to deal in the Software without restriction, including  
# without limitation the rights to use, copy, modify, merge, publish,  
# distribute, sublicense, and/or sell copies of the Software, and to  
# permit persons to whom the Software is furnished to do so, subject to  
# the following conditions:  
#  
# The above copyright notice and this permission notice shall be  
# included in all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE  
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
FROM alpine:3.7  
MAINTAINER Sean Quinn "sean.quinn@extesla.com"  
RUN apk update  
RUN apk add --no-cache ack bash curl gpgme sudo su-exec tzdata wget \  
&& rm -rf /var/cache/apk/* \  
&& chmod u+s /bin/su /sbin/su-exec  
  
#: Create a more friendly bash command line for when we have to actually  
#: enter a container during development or to debug.  
ADD files/etc/profile /etc/profile  
ADD files/.bashrc /root/.bashrc  

