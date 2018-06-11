FROM centos/systemd:latest  
MAINTAINER Kaushal M kshlmster@gmail.com  
  
ADD ./build.sh /  
RUN /build.sh && rm /build.sh  
  
CMD ["/usr/sbin/init"]  

