FROM debian:jessie  
  
RUN VERSION=0.5.0 \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -y install wget ca-certificates \  
&& wget https://github.com/bosun-
monitor/bosun/releases/download/$VERSION/bosun-linux-amd64 -O /bosun -nv \  
&& chmod +rx /bosun \  
&& apt-get -y purge --auto-remove wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
ENTRYPOINT ["/bosun", "-disable-syslog"]  
CMD ["-h"]  
EXPOSE 8070  
VOLUME /data  

