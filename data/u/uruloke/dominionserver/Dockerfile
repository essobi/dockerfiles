FROM python  
MAINTAINER Oliver Nybroe <olivernybroe@gmail.com>  
  
VOLUME /data  
EXPOSE 6700  
RUN pip install numpy  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  

