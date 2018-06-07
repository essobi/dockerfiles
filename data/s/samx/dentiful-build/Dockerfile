FROM ubuntu:15.04  
RUN apt-get update  
RUN apt-get install -y curl  
  
# Install Go  
RUN curl https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz |
tar -C /usr/local -zxvf -  
  
# Install PhantomJS  
RUN apt-get install -y libicu52 libjpeg8 libfontconfig1 libwebp5 libssl1.0.0
unzip  
RUN curl -o phantomjs.zip --location
https://github.com/bprodoehl/phantomjs/releases/download/v2.0.0-20150528/phantomjs-2.0.0-20150528-u1404-x86_64.zip  
RUN unzip phantomjs.zip && rm -v phantomjs.zip && mv phantomjs-2.0.0-20150528
/opt/phantomjs  
  
# Install Node.js  
RUN curl http://nodejs.org/dist/v0.12.4/node-v0.12.4-linux-x64.tar.gz | tar
-zxvf - && \  
mv node-v0.12.4-linux-x64 /opt/nodejs  
  
ENV PATH=/opt/phantomjs/bin:/usr/local/go/bin:/opt/nodejs/bin:$PATH  
  
RUN apt-get update && apt-get install -y git  

