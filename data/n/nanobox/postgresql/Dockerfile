# -*- mode: Dockerfile; tab-width: 4;indent-tabs-mode: nil;-*-  
# vim: ts=4 sw=4 ft=Dockerfile et: 1  
FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p /var/log/gonano  
  
# Install binaries  
RUN rm -rf /data/var/db/pkgin && \  
/data/bin/pkgin -y up && \  
/data/bin/pkgin -y in \  
yoke \  
postgresql94-adminpack \  
postgresql94-client \  
postgresql94-datatypes \  
postgresql94-dblink \  
postgresql94-fuzzystrmatch \  
postgresql94-monitoring \  
postgresql94-pgcrypto \  
postgresql94-plperl \  
postgresql94-plpython \  
postgresql94-pltcl \  
postgresql94-replicationtools \  
postgresql94-server \  
postgresql94-upgrade && \  
rm -rf /data/var/db/pkgin/cache  
  
# Install hooks  
RUN rm -rf /var/gonano/db/pkgin && \  
/opt/gonano/bin/pkgin -y up && \  
/opt/gonano/bin/pkgin -y in \  
hooks-postgresql && \  
rm -rf /var/gonano/db/pkgin/cache  
  
# Cleanup disk  
RUN rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Run runit automatically  
CMD /opt/gonano/bin/nanoinit  

