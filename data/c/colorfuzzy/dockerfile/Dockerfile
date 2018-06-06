FROM ubuntu:14.04  
MAINTAINER color.fuzzy  
  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-dev build-essential  
RUN apt-get install -y libmemcached-dev libxml2-dev libxslt1-dev libffi-dev
libssl-dev libgeos-dev binutils libtiff5-dev libjpeg8-dev zlib1g-dev
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk  
RUN pip install virtualenv  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

