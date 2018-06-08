FROM debian:latest  
MAINTAINER Santiago Sanchez Paz <sanchezpaz@gmail.com>  
# DESC streams public tweets matching the given keywords on the
twitter_streaming.py file. Works with tweepy==2.3.0.  
RUN apt-get update && apt-get -y install python python-pip python-yaml && pip
install tweepy==2.3.0  
  
# cleaning  
RUN apt-get -y autoclean && \  
apt-get -y --purge autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD twitter_stream.py /root/  
  
CMD python /root/twitter_stream.py  
  
# docker run --rm -v /myStorage/keys.yml:/root/keys.yml saintd/twitter-stream  

