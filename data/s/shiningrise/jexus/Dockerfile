FROM ubuntu:latest  
#Jexus V5.8.2 Beta1 64位独立版  
MAINTAINER shiningrise shiningrise@gmail.com  
  
ENV JEXUS_VERSION 5.8.2  
ADD jexus-${JEXUS_VERSION}-x64.tar.gz /usr/  
RUN mkdir /data  
RUN sed -i "s/root=\/ \/var\/www\/default/root=\/ \/data/g"
/usr/jexus/siteconf/default  
  
VOLUME ["/data"]  
EXPOSE 80 443  
CMD /usr/jexus/jwss  

