FROM debian:latest  
  
MAINTAINER letssudormrf  
  
  
#Download applications  
RUN apt-get update \  
&& apt-get install -y libsodium-dev python git ca-certificates iptables --no-
install-recommends  
  
#Make ssr-mudb  
ENV USER="MUDB"  
ENV PORT="443"  
ENV PASSWORD="ssr-lkl-docker"  
ENV METHOD="chacha20"  
ENV PROTOCOL="auth_aes128_md5"  
ENV OBFS="tls1.2_ticket_auth"  
RUN git clone https://github.com/shadowsocksr/shadowsocksr.git \  
&& cd shadowsocksr \  
&& bash initcfg.sh \  
&& sed -i 's/sspanelv2/mudbjson/' userapiconfig.py \  
&& python mujson_mgr.py -a -u ${USER} -p ${PORT} -k ${PASSWORD} -m ${METHOD}
-O ${PROTOCOL} -o ${OBFS} -G "#"  
  
#Execution environment  
COPY liblkl-hijack.so start.sh /root/  
RUN chmod a+x /root/liblkl-hijack.so /root/start.sh  
WORKDIR /shadowsocksr  
ENTRYPOINT ["/root/start.sh"]  

