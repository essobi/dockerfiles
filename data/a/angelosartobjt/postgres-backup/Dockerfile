FROM debian:jessie  
  
#install cron, s3cmd for copying to amazon, and postgres client for running
dump  
RUN apt-get update && apt-get install -y vim  
RUN apt-get update && apt-get install -y cron  
RUN apt-get update && apt-get install -y curl && apt-get install -y s3cmd  
# Used for testing by overriding the clock and running the backup scripts.  
RUN apt-get update && apt-get install -y libfaketime  
  
RUN set -ex; \  
# pub 4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]  
# Key fingerprint = B97B 0AFC AA1A 47F0 44F2 44A0 7FCC 7D46 ACCC 4CF8  
# uid PostgreSQL Debian Repository  
key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/postgres.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
ENV PG_MAJOR 9.6  
ENV PG_VERSION 9.6.2-1.pgdg80+1  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& apt-get install -y \  
postgresql-$PG_MAJOR=$PG_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
#copy in environment generation script  
COPY start.sh /root/start.sh  
RUN chmod u+x /root/start.sh  
  
#copy in core backup script, make executable  
COPY backup* /root/  
RUN chmod u+x /root/backup*  
  
#copy in cron configuration  
COPY backup-cron /etc/cron.d/backup-cron  
RUN touch /var/log/backup.log  
  
CMD ["/root/start.sh"]  

