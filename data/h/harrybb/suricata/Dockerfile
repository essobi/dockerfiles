# suricata dockerfile by MO  
#  
# VERSION 16.10  
FROM ubuntu:16.04  
MAINTAINER MO  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ 'Asia/Kolkata'  
  
# Include dist  
ADD dist/ /root/dist/  
# Setup apt  
RUN echo "deb http://ppa.launchpad.net/oisf/suricata-stable/ubuntu xenial
main" >> /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/oisf/suricata-stable/ubuntu xenial
main" >> /etc/apt/sources.list && \  
echo $TZ > /etc/timezone && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
9F6FC9DDB1324714B78062CBD7F87B2966EB736F && \  
apt-get update -y && \  
apt-get upgrade -y && \  
  
# Install packages  
apt-get install -y net-tools tzdata supervisor suricata wget make gcc libpcap-
dev libjansson-dev git && \  
cd /opt/ && \  
git clone https://github.com/t3chn0m4g3/p0f -b json-logging && \  
cd p0f && \  
./build.sh && \  
  
# Setup user, groups and configs  
addgroup \--gid 2000 tpot && \  
adduser \--system \--no-create-home \--shell /bin/bash \--uid 2000
\--disabled-password \--disabled-login \--gid 2000 tpot && \  
mv /root/dist/supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \  
mv /root/dist/suricata.yaml /etc/suricata/suricata.yaml && \  
mv /root/dist/rules/* /etc/suricata/rules/ && \  
  
# Download the latest EmergingThreats ruleset  
# wget --no-parent -l1 -r --no-directories -P /etc/suricata/rules/
https://rules.emergingthreats.net/open/suricata/rules/ && \  
# Clean up  
rm -rf /root/* && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
apt-get purge -y make gcc libpcap-dev libjansson-dev git && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start suricata  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

