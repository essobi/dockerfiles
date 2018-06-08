FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV ENV INITRD No  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
ENV PHANTOMJS_VERSION 2.1.1  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y git-core libfreetype6 libfontconfig python  
WORKDIR /sev  
ADD
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
/srv/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2  
RUN tar jxvf /srv/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 -C
/usr/local/  
RUN ln -sf
/usr/local/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN git clone https://github.com/casperjs/casperjs.git /usr/local/casperjs  
RUN ln -sf /usr/local/casperjs/bin/casperjs /usr/local/bin/casperjs  

