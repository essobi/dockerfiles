FROM debian:wheezy  
  
MAINTAINER Camil Blanaru <camil@edka.io>  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -yq runit wget python-httplib2 && \  
apt-get autoremove && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CB_VERSION=4.0.0 \  
CB_RELEASE_URL=http://packages.couchbase.com/releases \  
CB_PACKAGE=couchbase-server-community_4.0.0-debian7_amd64.deb \  
CB_SHA256=1FB8961E54B0E4A9D1FC2EFC925B82054281ABF3C520294311D874E66D78CF6E \  
PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install
\  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/couchbase/lib  
  
# Create Couchbase user with UID 1000  
RUN groupadd -g 1000 couchbase && useradd couchbase -u 1000 -g couchbase -M  
  
# Install couchbase  
RUN wget -N $CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE && \  
echo "$CB_SHA256 $CB_PACKAGE" | sha256sum -c - && \  
dpkg -i ./$CB_PACKAGE && rm -f ./$CB_PACKAGE  
  
# Add runit script for couchbase-server  
COPY scripts/run /etc/service/couchbase-server/run  
  
# Add bootstrap script  
COPY scripts/entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["couchbase-server"]  
  
EXPOSE 8091 8092 8093 11207 11210 11211 18091 18092  
VOLUME /opt/couchbase/var  
  

