FROM debian:wheezy  
  
MAINTAINER developers@synopsis.cz  
  
RUN apt-get update && apt-get install -y centerim-utf8 && apt-get clean  
  
RUN apt-get update && apt-get install -y imagemagick && apt-get clean  
  
RUN apt-get update && apt-get install -y php5-cli && apt-get clean  
  
RUN apt-get update && apt-get install -y screen && apt-get clean  
  
VOLUME /root/.centerim  
  
WORKDIR /root  
  
CMD [centerim-utf8]  

