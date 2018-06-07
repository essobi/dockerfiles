from centos:7  
ENV container docker  
RUN yum -y install bzip2 which rsync nfs-utils initscripts  
STOPSIGNAL SIGRTMIN+3  
EXPOSE 8443  
CMD [ "/sbin/init" ]  

