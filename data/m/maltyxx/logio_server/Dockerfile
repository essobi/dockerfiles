FROM node:0.12  
  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
# add our user and group  
RUN useradd --create-home --home-dir /home/logio --shell /bin/false \--user-
group logio  
  
RUN export USER=logio \  
&& export HOME=/home/logio \  
&& npm install -g log.io --user "logio"  
  
EXPOSE 28777 28778  
  
WORKDIR /home/logio  
  
USER logio  
  
CMD log.io-server

