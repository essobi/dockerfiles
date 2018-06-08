FROM debian:sid  
  
LABEL author "Korviakov Andrey"  
LABEL maintainer "4lifenet@gmail.com"  
  
LABEL SERVICE_NAME "munin-node"  
  
HEALTHCHECK CMD nc -zv localhost 4949  
  
#Config for gathering host metrics  
ENV HOST_DEV_DIR=/host/dev \  
HOST_PROC_DIR=/host/proc \  
HOST_SYS_DIR=/host/sys  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
tzdata \  
munin-node \  
munin-async \  
python-beanstalkc \  
netcat \  
jq \  
bc \  
curl \  
net-tools \  
libwww-perl \  
&& ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime \  
&& apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
/usr/share/doc/* /etc/munin/* \  
&& mkdir /etc/munin/plugins  
  
COPY bin/ bin/  
COPY conf/ /etc/munin  
COPY plugins/ /usr/share/munin/plugins/  
  
VOLUME /var/lib/munin-async /var/lib/munin-node  
  
EXPOSE 4949  
CMD ["entrypoint.sh"]  

