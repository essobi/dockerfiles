FROM ubuntu:16.04  
MAINTAINER Brian Freeman <brian.freeman@panoply.fm>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV BUILD_PACKAGES postgresql-9.6-citus-6.1 postgresql-contrib  
  
RUN set -ex && \  
apt-get -y update && \  
apt-get install -y curl  
  
RUN set -ex && \  
curl https://install.citusdata.com/community/deb.sh | bash && \  
apt-get -y update && \  
apt-get install -y --no-install-recommends $BUILD_PACKAGES && \  
rm -rf /var/lib/apt/lists/*  
  
# add build scripts  
Add scripts/init_db.sh /scripts/init_db.sh  
RUN chmod +x /scripts/init_db.sh  
  
Add scripts/start_db.sh /scripts/start_db.sh  
RUN chmod +x /scripts/start_db.sh  
  
USER postgres  
RUN /bin/bash /scripts/init_db.sh  
  
RUN echo "host all all 0.0.0.0/0 trust" >>
/var/lib/postgresql/citus/master/pg_hba.conf  
RUN echo "listen_addresses='*'" >>
/var/lib/postgresql/citus/master/postgresql.conf  
  
EXPOSE 9700  
CMD /bin/bash /scripts/start_db.sh  

