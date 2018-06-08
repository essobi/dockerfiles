FROM selenium/standalone-firefox  
  
USER root  
  
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
  
RUN chmod -v a+rx \  
/usr/local/bin/cloe_run  
  
ENV CLOE_RUN_BIN=/opt/bin/entry_point.sh  
  
ENTRYPOINT [ "/usr/local/bin/cloe_run" ]  

