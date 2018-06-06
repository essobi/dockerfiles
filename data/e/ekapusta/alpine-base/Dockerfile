FROM alpine  
MAINTAINER Alexander Ustimenko "http://ustimen.co/"  
# Copy tools to /usr/bin  
COPY bin/* /usr/bin/  
  
RUN \  
# Init custom run and volumes dirs  
mkdir -p /dcr/cm.d /dcr/vol && \  
# Make sure copied files are executable  
chmod +x /usr/bin/VOL*  
  
# Add hooks on before main command stage  
COPY cm.d/* /dcr/cm.d/  
  
# Allows us to read environment variables in CMD  
ENTRYPOINT ["/bin/sh", "-c"]  
  
# Allows us to customize default CMD by adding pre/post hooks  
CMD ["for CMD in /dcr/cm.d/*; do source $CMD; done"]  

