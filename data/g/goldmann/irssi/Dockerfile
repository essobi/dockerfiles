FROM centos:latest  
RUN yum -y update && yum -y install irssi && yum clean all  
RUN useradd -m irssi  
RUN ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
ENV SCREENDIR /home/irssi/screen  
USER irssi  
WORKDIR /home/irssi  
VOLUME "/home/irssi/data"  
CMD ["irssi", "--home", "/home/irssi/data"]  

