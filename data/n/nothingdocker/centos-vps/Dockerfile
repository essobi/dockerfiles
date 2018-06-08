# Version 1.0.0  
FROM nothingdocker/centos-systemd  
RUN set -x \  
&& yum -y install nginx \  
&& curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" \  
&& python /tmp/get-pip.py \  
&& pip install --upgrade pip \  
&& pip install shadowsocks \  
&& yum clean all  
COPY shadowsocks.json /etc/shadowsocks.json  
COPY shadowsocks.service /etc/systemd/system/shadowsocks.service  
RUN systemctl enable shadowsocks.service  
RUN set -x \  
&& yum install -y openvpn \  
&& yum install -y easy-rsa \  
&& yum install -y firewalld \  
&& cp -R /usr/share/easy-rsa/ /etc/openvpn \  
&& yum clean all \  
&& systemctl enable openvpn@server  
COPY openvpn-server.conf /etc/openvpn/server.conf  
COPY easy-rsa-vars /etc/openvpn/easy-rsa/2.0/vars  
COPY keys/* /etc/openvpn/  
COPY autorun.service /etc/systemd/system/autorun.service  
COPY autorun /autorun  
RUN systemctl enable autorun.service  
EXPOSE 15002 15003  

