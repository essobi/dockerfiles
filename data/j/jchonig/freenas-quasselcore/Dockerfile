FROM phusion/baseimage:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="0.12.4" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.privileged="false" \  
org.freenas.port-mappings="4242:4242/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Quassel data directory\" \  
} \  
]"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-add-repository ppa:mamarley/quassel \  
&& apt-get update \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confold" \  
&& apt-get install -y quassel-core \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/quasselcore  
COPY quasselcore /etc/service/quasselcore/run  
RUN chmod +x /etc/service/quasselcore/run  
  
VOLUME ["/config"]  
EXPOSE 4242  
  

