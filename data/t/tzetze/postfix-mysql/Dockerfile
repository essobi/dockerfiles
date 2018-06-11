FROM ubuntu:14.04  
RUN apt-get update && apt-get -y -q install postfix  
  
ADD run.sh /run.sh  
  
expose 25  
cmd ["/run.sh"]  
  

