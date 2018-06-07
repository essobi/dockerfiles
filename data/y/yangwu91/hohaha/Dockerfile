FROM rastasheep/ubuntu-sshd:16.04  
MAINTAINER yangwu91 yangwu91@outlook.com  
  
RUN apt update && \  
apt install -y python \  
gcc \  
libsodium18 \  
curl \  
openssh-server \  
git \  
tzdata \  
ntp \  
libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 2222  
# net-speeder  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
RUN mv net_speeder /usr/local/bin/  
RUN chmod +x /usr/local/bin/net_speeder  
  
# SSR server  
RUN mkdir -p /opt  
COPY ssr-custom /opt/ssr-custom  
COPY user-config.json /opt/ssr-custom/  
COPY dns.conf /opt/ssr-custom/  
RUN find /opt/ssr-custom/ -name "*.sh" -type f | xargs -I {} chmod +x {}  
RUN mkdir -p /var/log/  
RUN touch /var/log/shadowsocksr.log  
  
# SSH  
RUN echo 'root:rootroot' |chpasswd  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /ssh  
COPY authorized_keys /ssh  
RUN sed -ri \  
-e 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' \  
-e 's/UsePAM yes/#UsePAM yes/g' \  
-e 's/^Port 22/Port 2222/g' \  
-e 's/#PasswordAuthentication yes/PasswordAuthentication no/g' \  
-e 's;^#AuthorizedKeysFile.+$;AuthorizedKeysFile /ssh/authorized_keys;g' \  
/etc/ssh/sshd_config  
  
# time zone  
RUN echo "America/New_York" > /etc/timezone  
  
# CN Source and DNS  
COPY CN_sources.list /opt/  
COPY CN_dns.conf /opt/  
  
COPY init.sh /opt/init.sh  
RUN chmod +x /opt/init.sh  
WORKDIR /  
  
ENTRYPOINT ["/opt/init.sh"]  
  

