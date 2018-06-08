FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y supervisor python3-pip wget bash
unzip openssh-server  
  
RUN pip3 install requests Flask  
  
ENV SS_PASSWORD kexueshangwang  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:kexueshangwang' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
WORKDIR /root/  
  
ADD shadowsocksR.sh /root/install-shadowsocks.sh  
RUN sh install-shadowsocks.sh  
#RUN wget --no-check-certificate -O shadowsocks-go.sh
https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-
go.sh && \  
# chmod +x shadowsocks-go.sh && \  
# ./shadowsocks-go.sh 2>&1 | tee shadowsocks-go.log  
ADD requirements.txt .  
  
RUN pip3 install -r requirements.txt  
  
RUN mkdir /root/kcptun  
  
ADD /kcptun/ /root/kcptun/  
  
EXPOSE 8989  
EXPOSE 6688/udp  
EXPOSE 5000  
ADD ss.conf /etc/supervisor/conf.d/ss.conf  
ADD kcp.conf /etc/supervisor/conf.d/kcp.conf  
ADD flask.conf /etc/supervisor/conf.d/flask.conf  
ADD sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
ADD code /root/code  
  
CMD supervisord -n

