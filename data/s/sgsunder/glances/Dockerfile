FROM debian:jessie-slim  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get -y install build-essential \  
curl \  
libfreetype6 \  
libfreetype6-dev \  
libpng12-0 \  
libpng12-dev \  
lm-sensors \  
pkg-config \  
python \  
python-dev \  
python-pip \  
&& pip install
"glances[action,browser,cpuinfo,chart,docker,export,folders,gpu,ip,raid,snmp,web]"
\  
&& apt-get remove -y build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
pkg-config \  
python-dev \  
&& rm -rf /root/.cache/pip /var/lib/apt/lists/*  
  
WORKDIR /etc/glances  
EXPOSE 61208 61209  
  
ENTRYPOINT ["python", "-m", "glances", "-w"]  

