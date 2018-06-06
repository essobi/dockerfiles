# Copyright 2016 Hewlett-Packard Development Company, L.P.  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy
of  
# this software and associated documentation files (the "Software"), to deal
in  
# the Software without restriction, including without limitation the rights to  
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies  
# of the Software, and to permit persons to whom the Software is furnished to
do  
# so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
FROM node:6.4  
# currently support only slack out of the box  
# to replace adapter: run with different ADAPTER env  
# and change ADAPTER env to new adapter name  
ENV ADAPTER slack  
  
RUN mkdir /bot && \  
useradd -ms /bin/bash node && \  
chown -R node /bot && \  
npm install -g yo@1.7.0 coffee-script eedevops/generator-hubot-
enterprise#2c2234052148d6d620b80a281a40b804da09fffc  
  
WORKDIR /bot  
ADD . /he  
RUN chmod u+wrx /he/script/docker_install.sh  
  
USER node  
  
RUN cd /bot && yo hubot-enterprise --defaults --location /he  
  
CMD ["/he/script/docker_install.sh"]  

