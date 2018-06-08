FROM jakexks/nodejs  
MAINTAINER Jake Sanders <i@am.so-aweso.me>  
  
ADD start.sh /start.sh  
RUN git clone https://github.com/magne4000/quassel-webserver.git && cd
quassel-webserver && npm install --production && chmod +x /start.sh && rm
/data/quassel-webserver/ssl/*  
  
WORKDIR /data/quassel-webserver  
EXPOSE 64080  
CMD ["/start.sh"]  

