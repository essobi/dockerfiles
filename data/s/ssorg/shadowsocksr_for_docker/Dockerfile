FROM centos:7.3.1611  
MAINTAINER shadowsocksr for docker <https://hub.docker.com/u/ssorg/>  
  
RUN yum install -y git; yum clean all  
RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git  
#WORKDIR /shadowsocksr  
#RUN sh initcfg.sh  
#WORKDIR /  
# test  
#RUN python /shadowsocksr/shadowsocks/server.py -k 1234 -d start  
#RUN python /shadowsocksr/shadowsocks/local.py -s 127.0.0.1 -k 1234 &  
#RUN curl --socks5 127.0.0.1:1080 google.com  
# net-speeder  
RUN yum install -y epel-release; yum clean all  
RUN yum install -y gcc libnet libpcap libnet-devel libpcap-devel git iproute;
yum clean all  
RUN git clone https://github.com/snooda/net-speeder.git  
WORKDIR /net-speeder  
#OpenVZ with -DCOOKED, KVM Xen RealPhysicalServer  
RUN sh build.sh  
WORKDIR /  
  
# supervisor  
RUN yum install -y python-setuptools; yum clean all  
RUN easy_install supervisor  
RUN echo_supervisord_conf > /etc/supervisord.conf  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
# run with -p XX:XX, not -P  
#EXPOSE  
ENTRYPOINT ["/entrypoint.sh"]  

