# Keepalived  
#  
# Keepalived is a routing software to provide simple and robust facilities for  
# loadbalancing and high-availability to Linux system  
#  
# NOTE: You need enable ip_vs module with command  
# sudo modprobe ip_vs  
# and run with parameters  
# --cap-add=NET_ADMIN --net=host -v /lib/modules:/lib/modules:ro  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install Keepalived from PPA  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
echo "deb http://ppa.launchpad.net/keepalived/stable/ubuntu \  
$(lsb_release -cs) main" \  
> /etc/apt/sources.list.d/keepalived-$(lsb_release -cs).list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7C33BDC6 && \  
apt-get update && \  
apt-get install -y keepalived && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
CMD ["keepalived", "--use-file", "/etc/keepalived/keepalived.conf", \  
"--dont-fork", "--log-console"]  
VOLUME ["/var/log", "/etc/keepalived"]  

