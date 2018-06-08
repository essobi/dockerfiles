FROM ubuntu:trusty  
  
MAINTAINER NAKAYAMA Masahiro <aki@nekoruri.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y git software-properties-common  
  
RUN mkdir -p /data/www/rawgit.com  
RUN git clone https://github.com/rgrove/rawgit.git /data/www/rawgit.com  
  
RUN /data/www/rawgit.com/scripts/bootstrap.sh  
  
WORKDIR /data/www/rawgit.com  
RUN npm install  
  
COPY init.sh /  
RUN chmod +x /init.sh  
CMD [ "/init.sh" ]  
  
EXPOSE 80 443  

