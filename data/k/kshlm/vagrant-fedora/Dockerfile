FROM fedora:latest  
MAINTAINER Kaushal M kshlmster@gmail.com  
  
ENV container docker  
  
ADD ./build.sh /  
RUN /build.sh && rm /build.sh  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  

