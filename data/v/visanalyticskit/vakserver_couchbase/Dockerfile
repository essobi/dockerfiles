#!/usr/bin/env docker  
FROM visanalyticskit/vakserver_base:latest  
MAINTAINER visanalyticskit@gmail.com  
  
# remove curl because there seem to be conflicts because cb-server ships with
curl  
RUN apt-get -q update && DEBIAN_FRONTEND=noninteractive && \  
apt-get remove -yq curl && \  
apt-get install -yq --no-install-recommends \  
python-httplib2 \  
inotify-tools && \  
  
apt-get autoclean && apt-get -y autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN groupadd -g 1000 couchbase && useradd couchbase -u 1000 -g couchbase -M  
  
#http://packages.couchbase.com/releases/4.0.0/couchbase-server-
community_4.0.0-ubuntu14.04_amd64.deb  
ENV CB_VERSION=4.0.0 \  
CB_RELEASE_URL=http://packages.couchbase.com/releases  
ENV CB_PACKAGE=couchbase-server-community_$CB_VERSION-ubuntu14.04_amd64.deb \  
PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install
\  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/couchbase/lib \  
CB_USER=desmond \  
CB_PASSWORD=secret_password \  
CB_RAMSIZE=1024 \  
CB_BUCKET=sync_gateway  
  
# Install couchbase  
RUN wget -N -q $CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE && \  
dpkg -i ./$CB_PACKAGE && rm -f ./$CB_PACKAGE  
  
# Add runit script for couchbase-server  
COPY scripts/run /etc/service/couchbase-server/run  
  
COPY /scripts /scripts  
RUN chmod +x /scripts/first_run.sh /etc/service/couchbase-server/run && \  
touch /firstrun  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 8091 8092 8093 11207 11210 11211 18091 18092  
VOLUME /opt/couchbase/var  

