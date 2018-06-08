FROM debian:latest  
  
# Install rspamd  
RUN apt-get update \  
&& export DEBIAN_FRONTEND="noninteractive" \  
&& apt-get install -y lsb-release wget gnupg openssl\  
&& CODENAME=`lsb_release -c -s` \  
&& wget -O- https://rspamd.com/apt-stable/gpg.key | apt-key add - \  
&& echo "deb http://rspamd.com/apt-stable/ $CODENAME main" >
/etc/apt/sources.list.d/rspamd.list \  
&& echo "deb-src http://rspamd.com/apt-stable/ $CODENAME main" >>
/etc/apt/sources.list.d/rspamd.list \  
&& apt-get update \  
&& apt-get --no-install-recommends install -y rspamd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY rspamd.conf /etc/rspamd  
  
COPY run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
  
# Port 11334 is for web frontend  
# Port 11332 is for milter  
# Port 11333 is for worker  
EXPOSE 11332 11334  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

