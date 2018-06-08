FROM ubuntu:14.04  
MAINTAINER setup1  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y openssh-server \  
&& echo 'root:32886/rzw' |chpasswd \  
&& mkdir /var/run/sshd \  
&& cp /etc/ssh/sshd_config /etc/ssh/sshd_config.b \  
&& echo 'PermitRootLogin yes' > /etc/ssh/sshd_config \  
&& apt-get install -y python-pip \  
&& pip install shadowsocks  
  
ADD run.sh /etc/run.sh  
RUN chmod +x /etc/run.sh \  
&& wget --no-check-certificate -P /etc https://wp.setupt.tk/config.json  
  
EXPOSE 443  
EXPOSE 22  
EXPOSE 201  
EXPOSE 202  
EXPOSE 203  
EXPOSE 204  
EXPOSE 205  
CMD /etc/run.sh && /usr/sbin/sshd -D

