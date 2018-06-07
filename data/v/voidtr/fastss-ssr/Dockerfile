FROM alpine:3.5  
MAINTAINER Tau'ri <tauri823@gmail.com>  
  
ENV HOME /root  
ENV DNS_ADDR 8.8.8.8  
  
RUN apk \--update add \--no-cache \  
git \  
py-pip \  
curl \  
&& pip install cymysql \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /root  
  
RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git  
RUN cp /root/shadowsocksr/apiconfig.py /root/shadowsocksr/userapiconfig.py  
  
COPY do.sh /root/  
RUN chmod +x /root/do.sh  
  
CMD /root/do.sh -h db_host -u db_user -p db_passwd -d db_name -m aes-256-cfb
-o tls1.2_ticket_auth -k passwd -t 443 -a api -s apisecret -l url

