FROM debian:jessie  
  
RUN VERSION=0.5.0 \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -y install wget ca-certificates python-pip \  
&& wget https://github.com/bosun-
monitor/bosun/releases/download/$VERSION/bosun-linux-amd64 -O /bosun -nv \  
&& chmod +rx /bosun \  
&& pip install envtpl \  
&& apt-get -y purge --auto-remove wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/bosun.conf.tpl /etc/bosun/bosun.conf.tpl  
COPY scripts/run.sh /run.sh  
RUN chmod +x /run.sh  
  
WORKDIR /data  
EXPOSE 8070  
VOLUME /data  
  
ENTRYPOINT ["/run.sh"]  

