  
FROM ubuntu:latest  
MAINTAINER Sylvain Savajols <s.savajols@gmail.com>  
  
ENV AP /home/visual-css-tester  
ENV PHANTOM_DIR /home/phantomjs  
  
## Intall apps  
RUN apt-get update -y  
RUN apt-get install -y \  
git \  
phantomjs \  
nodejs=0.10.25~dfsg2-2ubuntu1 \  
npm=1.3.10~dfsg-1 \  
python=2.7.5-5ubuntu3  
  
## Installation node  
RUN ln -sf /usr/bin/nodejs /usr/bin/node  
  
## Installation casperJS 1.0.4  
RUN git clone \--branch 1.0.4 git://github.com/n1k0/casperjs.git /opt/casperjs  
RUN ln -sf /opt/casperjs/bin/casperjs /usr/bin/  
  
## Installation sample visual css tester project  
RUN git clone \--branch 1.0.2 https://github.com/ssavajols/visual-css-
tester.git $AP  
  
WORKDIR $AP/  
  
## Install node modules  
RUN npm install  
RUN npm install -g phantomjs@1.8.x  
  
## copy node module to root path.  
## This node module could be overrided by app  
## if got his own visual-css-tester module  
## installed on the app folder.  
## Node recursively loop until the root dir to find  
## node_modules packages  
RUN cp -rf ./node_modules /node_modules  
  
## Désinstaller les applications inutiles  
RUN apt-get -y remove \  
git \  
npm  
  
CMD ["nodejs", "app.js"]  
#CMD ["/bin/bash"]  
#License MIT :  
#Copyright (c) 2015 : Savajols Sylvain  
#Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  
#The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.  
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  

