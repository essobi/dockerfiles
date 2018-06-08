FROM debian:stable  
  
RUN apt-get update && apt-get install -y gettext-base python-pip curl git  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
curl -sk https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&
\  
apt-get update && apt-get install --no-install-recommends -y postgresql-
client-9.3 && \  
apt-get clean -y  
  
WORKDIR /app  
RUN curl -sSL -o /usr/local/bin/etcdctl https://s3-us-
west-2.amazonaws.com/opdemand/etcdctl-v0.4.6 && chmod +x
/usr/local/bin/etcdctl  
RUN pip install python-dateutil; pip install
git+https://github.com/s3tools/s3cmd  
COPY backup.sh /app/backup.sh  
COPY s3cfg /app/s3cfg  
CMD ./backup.sh

