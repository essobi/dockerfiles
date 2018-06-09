FROM centos:centos7  
ENV CB_VERSION 4.5.0  
ENV CB_RELEASE_URL http://packages.couchbase.com/releases  
ENV CB_PACKAGE couchbase-server-enterprise-4.5.0-centos7.x86_64.rpm  
# Add couchbase binaries to PATH  
ENV PATH
$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install  
# Install yum dependencies  
RUN yum install -y hostname initscripts openssl pkgconfig sudo tar wget lsof
netstat curl  
# Install couchbase  
#add couchbase user  
RUN useradd -m couchbase  
RUN rpm --install $CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE  
USER couchbase  
COPY ./docker-entrypoint.sh /  
VOLUME ["/opt/couchbase/var"]  
EXPOSE 8091 8092 8093 8094 11207 11210 11211 18091 18092 18093  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

