FROM centos:latest  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN yum -y install epel-release && \  
yum -y update && \  
yum -y install rtorrent  
  
ADD ./rctorrent.rc /rtorrent/  
ADD ./start.sh /start.sh  
  
RUN mv /rtorrent/rctorrent.rc /root/.rctorrent.rc  
RUN mkdir ~/.rtorrent  
  
RUN chmod u+x /start.sh  
  
EXPOSE 33101-33199  
CMD ["./start.sh"]  

