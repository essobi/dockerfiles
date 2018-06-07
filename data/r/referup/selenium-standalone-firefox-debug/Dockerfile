FROM selenium/standalone-firefox-debug:2.53.0  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
daemontools \  
inotify-tools \  
moreutils \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY cloe_run /usr/local/bin/cloe_run  
  
RUN \  
chmod +x \  
/usr/local/bin/cloe_run  
  
ENTRYPOINT [ "/opt/bin/entry_point.sh" ]  

