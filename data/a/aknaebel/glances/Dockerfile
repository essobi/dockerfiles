FROM alpine:latest  
MAINTAINER Alain Knaebel, <alain.knaebel@aknaebel.fr>  
  
#ENV ISSO_SETTINGS /opt/isso/isso.conf  
RUN apk upgrade --update \  
&& apk add python3 python3-dev gcc g++ linux-headers musl-dev ca-certificates
openssl freetype-dev libpng-dev \  
&& update-ca-certificates \  
&& pip3 install
glances[action,browser,cloud,cpuinfo,chart,docker,export,folders,gpu,ip,raid,snmp,web,wifi]
\  
&& mkdir -p /glances/conf \  
&& apk del python3-dev gcc g++ linux-headers freetype-dev libpng-dev \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
WORKDIR /glances  
  
# EXPOSE PORT (For XMLRPC)  
EXPOSE 61209  
# EXPOSE PORT (For Web UI)  
EXPOSE 61208  
# Define default command.  
CMD python3 -m glances -C /glances/conf/glances.conf $GLANCES_OPT  

