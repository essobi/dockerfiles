FROM alpine:3.3  
MAINTAINER o_tee_one <o_tee_one@r0x.tw>  
  
ENV PASSWORD "changeme"  
ENV GAME_NAME "r0x.tw - new server"  
ENV GAME_TYPE "blocker"  
ENV MAX_CLIENTS 64  
ENV GAME_MAP "blmapV3"  
RUN apk add --update pwgen openssl python g++ bam bash unzip \  
&& rm -rf /var/cache/apk/*  
RUN cd / \  
&& wget https://github.com/ddnet/ddnet/archive/master.zip \  
&& unzip master.zip  
RUN cd ddnet-master \  
&& bam server_release \  
&& cd /  
  
COPY blmapV3.map /ddnet-master/data/maps/blmapV3.map  
COPY run.bash /run.bash  
COPY ddrace.cfg /ddrace.cfg  
COPY blocker.cfg /blocker.cfg  
  
RUN chmod +x /run.bash  
  
EXPOSE 8303/udp  
CMD ["/run.bash"]  

