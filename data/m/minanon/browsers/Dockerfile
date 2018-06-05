FROM debian  
  
ENV PHANTOM_VERSION 2.1.1  
RUN apt update \  
&& apt install -y curl bzip2  
  
RUN apt install -y firefox-esr chromium  
  
RUN cd tmp \  
&& curl -L
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_VERSION}-linux-x86_64.tar.bz2"
\  
| tar -jx phantomjs-${PHANTOM_VERSION}-linux-x86_64/bin/phantomjs \  
&& mv phantomjs-${PHANTOM_VERSION}-linux-x86_64/bin/phantomjs /usr/local/bin \  
&& rm -rf phantomjs-${PHANTOM_VERSION}-linux-x86_64  

