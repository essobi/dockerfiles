FROM ubuntu:16.04  
RUN apt-get update -qq && apt-get -y upgrade  
RUN apt-get install -y python-pip python-m2crypto python-gevent python-
setuptools openssh-server nano wget curl iptables  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN export LC_ALL=C  
RUN pip install shadowsocks  
#RUN mkdir /etc/shadowsocks  
ADD shadowsocks.json /etc/shadowsocks.json  
  
RUN mkdir -p /opt/kcptun && cd /opt/kcptun  
RUN wget https://github.com/xtaci/kcptun/releases/download/v20170120/kcptun-
linux-amd64-20170120.tar.gz  
RUN tar -zxf kcptun-linux-amd64-20170120.tar.gz  
RUN rm -rf kcptun-linux-amd64-20170120.tar.gz  
ADD server.json /opt/kcptun/server.json  
ADD start.sh /opt/kcptun/start.sh  
ADD stop.sh /opt/kcptun/stop.sh  
ADD restart.sh /opt/kcptun/restart.sh  
ADD server_linux_amd64 /opt/kcptun/server_linux_amd64  
RUN chmod +x /opt/kcptun/server_linux_amd64  
  
RUN mkdir -p /opt/goflyway && cd /opt/goflyway  
ADD goflyway /opt/goflyway/goflyway  
ADD ca.pem /opt/goflyway/ca.pem  
RUN chmod +x /opt/goflyway/goflyway  
  
RUN mkdir /var/run/sshd  
RUN mkdir -p /root/.ssh  
ADD id_rsa.pub /root/.ssh/  
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
#RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config  
EXPOSE 22  
EXPOSE 443  
EXPOSE 33067/udp  
EXPOSE 80  
EXPOSE 8080  
EXPOSE 8880  
EXPOSE 8890  
EXPOSE 2086  
ADD run.sh /run.sh  
RUN chmod +x run.sh  
CMD ["/run.sh"]  
ENV HOME /  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

