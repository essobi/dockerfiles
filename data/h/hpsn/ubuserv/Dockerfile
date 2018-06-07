FROM library/ubuntu:rolling  
MAINTAINER harman.nagra@gmail.com  
  
# Download and install all packages  
RUN apt-get -y update \  
&& apt-get install -y isc-dhcp-server \  
&& apt-get install -y bind9 dnsutils \  
&& apt-get install -y nginx \  
&& apt-get install -y ssmtp smokeping fcgiwrap \  
&& apt-get install -y curl \  
&& apt-get install -y supervisor  
  
# Download and copy Speedtest probe - https://github.com/mad-ady/smokeping-
speedtest  
RUN \  
curl -L -o /usr/share/perl5/Smokeping/probes/speedtest.pm
https://github.com/mad-ady/smokeping-speedtest/raw/master/speedtest.pm  
  
# Download and copy speedtest-cli - https://github.com/sivel/speedtest-cli  
RUN \  
curl -L -o /usr/local/bin/speedtest-cli
https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py \  
&& chmod a+x /usr/local/bin/speedtest-cli  
  
ENV TZ=Etc/GMT  
ENV DATA_DIR=/data  
  
ENV DHCPD_ENABLED=false  
ENV BIND_ENABLED=true  
ENV NGINX_ENABLED=true  
ENV SMOKEPING_ENABLED=true  
  
RUN mkdir -p /supervisor-confs  
RUN mkdir -p /nginx-confs  
  
COPY data/supervisor-confs/supervisor-bind.conf /supervisor-confs  
COPY data/supervisor-confs/supervisor-dhcpd.conf /supervisor-confs  
COPY data/supervisor-confs/supervisor-nginx.conf /supervisor-confs  
COPY data/supervisor-confs/supervisor-smokeping.conf /supervisor-confs  
COPY data/supervisor-confs/supervisor-fcgiwrap.conf /supervisor-confs  
  
COPY data/nginx-confs/smokeping.include /nginx-confs  
  
COPY data/smokeping-fix/Smokeping.pm /usr/share/perl5/Smokeping.pm  
  
VOLUME ["/data"]  
  
COPY ubuserv.sh /sbin/ubuserv.sh  
RUN chmod 755 /sbin/ubuserv.sh  
  
EXPOSE 53/udp 53/tcp 8888/tcp  
  
ENTRYPOINT ["/sbin/ubuserv.sh"]  
  

