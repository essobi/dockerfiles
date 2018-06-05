FROM ubuntu:latest  
MAINTAINER Artistan <karl.tobias@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH $PATH:/usr/local/nginx/sbin  
  
# create directories  
RUN mkdir /src && mkdir /config && mkdir /logs && mkdir /data && mkdir /static  
  
# update and upgrade packages  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
RUN apt-get install -y build-essential wget apt-utils unzip  
  
# ffmpeg  
RUN apt-get install -y software-properties-common  
#RUN add-apt-repository ppa:mc3man/trusty-media  
RUN apt-get update  
RUN apt-get install -y ffmpeg  
  
# nginx dependencies  
RUN apt-get install -y libpcre3-dev zlib1g-dev libssl-dev  
RUN apt-get install -y wget  
  
# get nginx source  
RUN cd /src && wget http://nginx.org/download/nginx-1.9.15.tar.gz && tar zxf
nginx-1.9.15.tar.gz && rm nginx-1.9.15.tar.gz  
  
# get nginx-rtmp module  
RUN cd /src && wget https://github.com/arut/nginx-rtmp-
module/archive/master.zip && unzip master.zip && rm master.zip  
  
# compile nginx  
RUN cd /src/nginx-1.9.15 && ./configure --add-module=/src/nginx-rtmp-module-
master --conf-path=/config/nginx.conf --error-log-path=/logs/error.log --http-
log-path=/logs/access.log  
RUN cd /src/nginx-1.9.15 && make && make install  
  
# Cleaning  
RUN apt-get clean  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
ADD nginx.conf /template/nginx.conf  
ADD static /static  
  
EXPOSE 80 1935  
VOLUME ["/config"]  
  
CMD ["/usr/local/bin/run.sh"]  

