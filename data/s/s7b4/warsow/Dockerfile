FROM debian:stretch  
LABEL maintainer="s7b4 <baron.stephane@gmail.com>"  
  
ENV GOSU_VERSION=1.10 \  
WS_USER=warsow \  
WS_VERSION=2.1.2  
ENV WS_HOME=/home/$WS_USER  
  
# set user/group IDs  
RUN groupadd -r "$WS_USER" \--gid=999 && useradd -r -g "$WS_USER" \--uid=999
"$WS_USER"  
  
# Base  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes \  
ca-certificates \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Gosu  
RUN curl -o /usr/local/sbin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& chmod +x /usr/local/sbin/gosu  
  
# Configs  
RUN mkdir -p /etc/warsow  
COPY config/* /etc/warsow/  
  
COPY scripts/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 44444 44400  
VOLUME $WS_HOME  

