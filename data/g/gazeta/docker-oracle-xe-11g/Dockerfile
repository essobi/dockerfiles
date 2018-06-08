FROM ubuntu:16.04  
MAINTAINER Wei-Ming Wu <wnameless@gmail.com>  
  
ENV NLS_LANG=POLISH_POLAND.EE8MSWIN1250  
  
ADD assets /assets  
RUN /assets/setup.sh  
  
EXPOSE 22  
EXPOSE 1521  
EXPOSE 8080  
CMD /usr/sbin/startup.sh && /usr/sbin/sshd -D  

