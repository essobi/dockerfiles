FROM wellsie/centos7  
MAINTAINER Jono Wells <_oj.io>  
  
ENV PHANTOMJS_VERSION 2.0  
  
RUN yum -y install \  
bison flex fontconfig-devel freetype-devel gcc gcc-c++ git gperf \  
libicu-devel libjpeg-devel libpng-devel make openssl-devel ruby \  
sqlite-devel && \  
  
yum -y clean all && \  
  
cd /usr/local && \  
git clone -b ${PHANTOMJS_VERSION} https://github.com/ariya/phantomjs.git && \  
cd phantomjs && \  
./build.sh \--confirm && \  
ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
CMD [ "/usr/bin/phantomjs" ]  

