FROM ubuntu:12.04  
MAINTAINER Kei Sato <kei-sato@meeetol.com>  
  
#################### mecab https://github.com/Kimtaro/docker-mecab  
# Build essentials  
RUN apt-get update  
RUN apt-get install -y curl build-essential  
  
# Mecab  
RUN curl -O https://mecab.googlecode.com/files/mecab-0.996.tar.gz  
RUN tar -xzf mecab-0.996.tar.gz  
RUN cd mecab-0.996; ./configure --enable-utf8-only; make; make install;
ldconfig  
  
# Ipadic  
RUN curl -O https://mecab.googlecode.com/files/mecab-
ipadic-2.7.0-20070801.tar.gz  
RUN tar -xzf mecab-ipadic-2.7.0-20070801.tar.gz  
RUN cd mecab-ipadic-2.7.0-20070801; ./configure --with-charset=utf8; make;
make install  
RUN echo "dicdir = /usr/local/lib/mecab/dic/ipadic" > /usr/local/etc/mecabrc  
  
# Clean up  
RUN apt-get remove -y build-essential  
RUN rm -rf mecab-0.996.tar.gz*  
RUN rm -rf mecab-ipadic-2.7.0-20070801*  
#################### mecab END  
  
#################### jubatus https://github.com/kotas/docker-jubatus-
classifier  
RUN echo "deb http://download.jubat.us/apt binary/" | tee
/etc/apt/sources.list.d/jubatus.list  
RUN apt-get update && apt-get install -y --force-yes jubatus  
RUN cp /opt/jubatus/share/jubatus/example/config/classifier/pa.json
/opt/jubatus/etc/jubatus.json  
RUN mkdir -p /opt/jubatus/data  
  
ADD ./run.sh /run.sh  
ADD opt/jubatus/etc /opt/jubatus/etc  
  
VOLUME ["/opt/jubatus/etc", "/opt/jubatus/data"]  
EXPOSE 9199  
CMD ["/run.sh", "-f", "/opt/jubatus/etc/jubatus.json", "-d",
"/opt/jubatus/data"]  
#################### jubatus END

