FROM mc2labs/nodejs  
MAINTAINER lipeilong <xxx@xxx.cn>  
  
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/' /etc/apt/sources.list  
  
RUN apt-get -y update  
RUN apt-get install -y vim nginx  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-h"]  

