FROM greatfox/ssh  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN apt-get -y install pptpd  
  
RUN echo 'localip 192.168.100.1 \n\  
remoteip 192.168.100.100-200\n' >> /etc/pptpd.conf  
RUN echo 'user * pass *\n' >> /etc/ppp/chap-secrets  
  
RUN echo 'service pptpd start' >> /initrc  
  
EXPOSE 47  
EXPOSE 1723  

