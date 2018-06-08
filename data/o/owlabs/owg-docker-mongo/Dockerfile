FROM mongo  
  
# jq is in wheezy-backports  
RUN echo 'deb http://http.debian.net/debian wheezy-backports main' >
/etc/apt/sources.list.d/wheezy-backports.list  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y jq  
ADD start_mongo.sh /root/  
  
WORKDIR /root  
CMD bash ./start_mongo.sh  

