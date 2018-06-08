FROM centos:7  
MAINTAINER docker@unxs.io  
  
ENV container docker  
  
#Prepare systemd  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
#Install required packages  
RUN yum -y install httpd; systemctl enable httpd.service  
RUN yum -y install git gcc make mysql-devel openssl-devel  
RUN yum -y install bind-utils  
RUN yum -y clean all  
RUN systemctl enable httpd.service  
  
#Start install  
RUN mkdir /home/unxs  
RUN mkdir -p /var/www/unxs/html  
RUN mkdir -p /var/www/unxs/logs  
  
#Get source and then install parts  
WORKDIR /home/unxs  
RUN git clone https://github.com/unxs0/unxsBind.git  
RUN git clone https://github.com/unxs0/unxsBase.git  
  
WORKDIR /home/unxs/unxsBase/unxsTemplateLib  
RUN make install  
  
WORKDIR /home/unxs/unxsBase/unxsCIDRLib  
RUN make install  
  
WORKDIR /home/unxs/unxsBase/unxsAdmin  
RUN cp -ia images /var/www/unxs/html/  
RUN cp -ia js /var/www/unxs/html/  
RUN cp -ia css /var/www/unxs/html/  
  
WORKDIR /home/unxs/unxsBind  
RUN cp -i images/dns.ico /var/www/unxs/html/images/  
RUN make local.h;  
#this creates a dependency with docker-compose.yml  
RUN sed -i -e 's/#define DBIP0 NULL/#define DBIP0 \"unxsbind-mysql\"/g'
local.h  
RUN sed -i -e 's/#define DBIP1 NULL/#define DBIP1 \"unxsbind-mysql\"/g'
local.h  
RUN make; install -s iDNS.cgi /var/www/unxs/html/iDNS.cgi  
  
#Modify httpd service  
COPY unxsbind.httpd.conf /etc/httpd/conf.d/  
RUN sed -i -e 's/^Listen 80/#Listen 80/g' /etc/httpd/conf/httpd.conf  
  
CMD ["/usr/sbin/init"]  
  
#Useful commands  
#docker build -t unxsio/unxsbind .  
#docker rm -f unxsbind;docker run --privileged --restart unless-stopped --link
unxsbind-mysql:unxsbind-mysql --volume /sys/fs/cgroup:/sys/fs/cgroup:ro --name
unxsbind -p 8088:8088 -d unxsio/unxsbind  
#  
#docker build -t unxsio/unxsbind .;docker rm -f unxsbind;docker-compose up -d;  

