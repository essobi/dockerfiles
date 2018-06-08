# -*- mode: Dockerfile; tab-width: 4;indent-tabs-mode: nil;-*-  
# vim: ts=4 sw=4 ft=Dockerfile et: 1  
FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p /var/log/gonano  
  
# Install binaries  
RUN rm -rf /data/var/db/pkgin && \  
/data/bin/pkgin -y up && \  
/data/bin/pkgin -y in \  
redis-2.8 && \  
rm -rf /data/var/db/pkgin/cache  
  
# Install hooks  
RUN rm -rf /var/gonano/db/pkgin && \  
/opt/gonano/bin/pkgin -y up && \  
/opt/gonano/bin/pkgin -y in \  
hooks-redis && \  
rm -rf /var/gonano/db/pkgin/cache  
  
# Cleanup disk  
RUN rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Run runit automatically  
CMD /opt/gonano/bin/nanoinit  

