FROM tutum/centos:latest  
RUN rm /run.sh; mkdir -p /var/log/tinyproxy; chmod 777 /var/log/tinyproxy;
mkdir -p /var/run/tinyproxy; chmod 777 /var/run/tinyproxy; mkdir -p
/etc/tinyproxy;  
ADD run.sh /run.sh  
ADD libproxychains4.so /usr/local/lib/libproxychains4.so  
ADD proxychains4 /usr/local/bin/proxychains4  
ADD tinyproxy /usr/local/bin/tinyproxy  
ADD tor.repo /etc/yum.repos.d/tor.repo  
ADD proxychains.conf /etc/proxychains.conf  
ADD tinyproxy.conf /etc/tinyproxy/tinyproxy.conf  
RUN chmod 755 /run.sh; yum install -y wget nano psmisc tor; chmod a+x
/usr/local/bin/proxychains4; chmod a+x /usr/local/bin/tinyproxy;  
EXPOSE 8888  
CMD "/run.sh"  

