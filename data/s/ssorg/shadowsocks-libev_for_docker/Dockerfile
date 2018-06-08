FROM centos:7.3.1611  
MAINTAINER shadowsocks-libev for docker <https://hub.docker.com/u/ssorg/>  
  
RUN yum install -y epel-release; yum clean all  
RUN yum install -y gcc gettext autoconf libtool automake make pcre-devel
asciidoc xmlto udns-devel libev-devel libsodium-devel mbedtls-devel; yum clean
all  
RUN curl -o /tmp/librehat-shadowsocks-epel-7.repo
https://copr.fedorainfracloud.org/coprs/librehat/shadowsocks/repo/epel-7/librehat-
shadowsocks-epel-7.repo  
RUN mv /tmp/librehat-shadowsocks-epel-7.repo /etc/yum.repos.d/  
RUN yum update -y; yum clean all  
RUN yum install -y shadowsocks-libev; yum clean all  
  
# net-speeder  
#RUN yum install -y epel-release; yum clean all  
RUN yum install -y gcc libnet libpcap libnet-devel libpcap-devel git iproute;
yum clean all  
RUN git clone https://github.com/snooda/net-speeder.git  
WORKDIR /net-speeder  
#OpenVZ with -DCOOKED, KVM Xen RealPhysicalServer  
RUN sh build.sh  
WORKDIR /  
  
# test  
#RUN /usr/bin/ss-server -k 1234 -p 8888 &  
#RUN /usr/bin/ss-local -k 1234 -p 8888 -s 127.0.0.1 -l 1080 &  
#RUN curl --socks5 127.0.0.1:1080 google.com  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
# run with -p XX:XX, not -P  
#EXPOSE  
ENTRYPOINT ["/entrypoint.sh"]  

