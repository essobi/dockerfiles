FROM ubuntu:trusty  
RUN apt-get update -qq && apt-get -y upgrade  
RUN apt-get install -y python-pip python-m2crypto python-gevent python-
setuptools openssh-server  
RUN pip install shadowsocks  
RUN mkdir /etc/shadowsocks  
ADD config.json /etc/shadowsocks/config.json  
RUN mkdir /var/run/sshd  
RUN echo 'root:zrgpasswd' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
EXPOSE 22  
EXPOSE 8387  
ADD run.sh /run.sh  
RUN chmod +x run.sh  
CMD ["/run.sh"]  
ENV HOME /  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

