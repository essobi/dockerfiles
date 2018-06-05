FROM ubuntu:14.04  
MAINTAINER Szilárd Pfeiffer "coroner@pfeifferszilard.hu"  
RUN apt-key adv --fetch-keys
http://download.opensuse.org/repositories/security:/Zorp:/6:/0:/11/xUbuntu_14.04/Release.key
\  
&& echo "deb
http://download.opensuse.org/repositories/security:/Zorp:/6:/0:/11/xUbuntu_14.04/
./" >/etc/apt/sources.list.d/zorp.list \  
&& apt-get update  
RUN mkdir /etc/zorp \  
&& touch /etc/zorp/dh.pem \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
zorp \  
zorp-modules \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/tmp/* \  
&& rm -rf /tmp/*  
  
ENV ZORP_CONFIG_DIR /etc/zorp/  
ADD policy.py $ZORP_CONFIG_DIR/policy.py  
  
COPY . /app/  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD [ \  
"/usr/sbin/zorp", \  
"--foreground", \  
"--no-syslog", \  
"--user", "zorp", \  
"--group", "zorp", \  
"--verbose", "3", \  
"--log-spec", "*.accounting:4,core.summary:4", \  
"--as", "default" \  
]  

