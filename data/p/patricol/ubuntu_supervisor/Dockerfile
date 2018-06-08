FROM patricol/ubuntu:Cuda  
  
USER root  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
supervisor && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
#COPY --chown=root:root extras/supervisord.conf /etc/#Not yet supported by
docker hub's automated builds, which use an outdated version of docker.  
COPY extras/supervisord.conf /etc/  
  
#COPY --chown=root:root extras/conf.d/*.conf /etc/supervisor/conf.d/#Not yet
supported by docker hub's automated builds, which use an outdated version of
docker.  
COPY extras/conf.d/*.conf /etc/supervisor/conf.d/  
  
RUN echo "#!/bin/bash\n" | tee /home/user/earlycommands.sh && \  
chmod +x /home/user/earlycommands.sh  
# Use this for configuration commands that might normally be in the
entrypoint.  
USER user  
CMD sudo /usr/bin/supervisord -c /etc/supervisord.conf -n

