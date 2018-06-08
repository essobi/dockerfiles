FROM ubuntu:14.04  
# Install packages  
ENV AUTHORIZED_KEYS **None**  
ENV TZ "Asia/Shanghai"  
ENV TERM xterm  
ENV HOME /root  
  
WORKDIR /root  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server pwgen byobu
curl htop unzip vim wget nginx  
  
### ss-panel  
RUN apt-get -y install git curl php5 php-guzzle php5-mysql nginx php5-fpm
supervisor  
RUN apt-get install -y python-pip python-m2crypto  
RUN pip install cymysql  
RUN pip install shadowsocks  
  
# sshd  
RUN mkdir -p /var/run/sshd && mkdir -p /opt/public/ && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
RUN rm -f /etc/nginx/sites-available/default  
  
ADD config/super.conf /etc/supervisor/conf.d/shadowsocks.conf  
ADD config/p.php /opt/public/p.php  
ADD config/ocp.php /opt/public/ocp.php  
ADD config/tzzt.php /opt/public/tzzt.php  
ADD config/404.html /opt/public/404.html  
  
ADD config/set_root_pw.sh /set_root_pw.sh  
ADD config/run.sh /run.sh  
ADD config/bash_profile /root/.bash_profile  
#ADD config/ss.tar.gz /root/ss.tar.gz  
ADD config/shadow /etc/shadow  
ADD config/default /etc/nginx/sites-available/default  
ADD config/config.json /etc/config.json  
  
RUN chmod +x /*.sh  
#RUN wget https://www.dropbox.com/s/jlmyyhjkyv4243m/freess.tar.gz -O
/root/ss.tar.gz  
RUN wget https://hi.i2u.pw/subash/freess.tar.gz -O /root/ss.tar.gz  
#ADD config/freess.tar.gz /root/ss.tar.gz  
RUN /bin/tar -xzvf /root/ss.tar.gz -C /root  
  
RUN apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
EXPOSE 22 80 443 8080 8443 8989  
CMD ["/usr/bin/supervisord"]  
  

