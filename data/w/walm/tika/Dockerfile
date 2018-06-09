FROM walm/java  
MAINTAINER Andreas Wålm "andreas@walm.net"  
RUN mkdir /setup  
ADD . /setup  
RUN /setup/install.sh  
ADD tika.sh /etc/service/tika/run  
ADD tika-meta.sh /etc/service/tika-meta/run  
CMD ["/sbin/my_init"]  
  
EXPOSE 4500  
EXPOSE 4501  

