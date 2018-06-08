# version 1.4-1  
# docker-version 0.9.1  
FROM phusion/baseimage:0.9.13  
MAINTAINER guruvan "guruvan@shastafareye.net"  
# We use a bootstrap script to avoid having temporary cache files and build  
# dependencies being committed and included into the docker image.  
ADD bootstrap.sh /tmp/  
RUN chmod +x /tmp/bootstrap.sh  
RUN /tmp/bootstrap.sh  
  
ADD fusioncoin.conf /root/.fusioncoin/  
ADD fusioncoind.run /etc/service/fusioncoind/run  
RUN chmod 600 /root/.fusioncoin/fusioncoin.conf ; chmod 700
/etc/service/fusioncoind/run  
  
EXPOSE 18491 8492  
#ENTRYPOINT [""]  
CMD ["/sbin/my_init"]  

