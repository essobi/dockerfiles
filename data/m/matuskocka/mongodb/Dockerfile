FROM registry.fedoraproject.org/f26-modular/boltron  
  
ENV NAME=mongodb \  
ARCH=x86_64 \  
VERSION=0 \  
RELEASE=1 \  
MONGODB_VERSION="3.4.3"  
LABEL MAINTAINER "Matus Kocka" <mkocka@redhat.com>  
LABEL summary="MongoDB, NoSQL database." \  
name="$FGC/$NAME" \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
description="MongoDB is a scalable, high-performance, open source NoSQL
database." \  
vendor="Fedora Project" \  
com.redhat.component="$NAME" \  
usage="docker run -e MONGODB_USER=<user_name> -e MONGODB_PASSWORD=<password>
-e MONGODB_DATABASE=<db_name> -e MONGODB_ADMIN_PASSWORD=<admin_password> -p
27017:27017 mongodb" \  
org.fedoraproject.component="mongodb" \  
authoritative-source-url="registry.fedoraproject.org" \  
io.k8s.description="MongoDB is a scalable, high-performance, open source NoSQL
database." \  
io.k8s.display-name="MongoDB 3.4.3" \  
io.openshift.tags="mongodb, db, database, nosql" \  
io.openshift.expose-services="27017"  
  
RUN dnf install -y --rpm --nodocs gettext policycoreutils bind-utils iproute
rsync tar findutils python3 && dnf clean all && \  
dnf install -y --nodocs mongodb && dnf clean all  
  
# Set paths to avoid hard-coding them in scripts.  
ENV HOME=/var/lib/mongodb \  
CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/mongodb  
  
ADD files /  
  
# Add help file  
COPY root /  
  
EXPOSE 27017  
CMD ["/usr/bin/run-mongod"]  
  
# Container setup from scl  
RUN touch /etc/mongod.conf && \  
mkdir -p ${HOME}/data && \  
# Set owner 'mongodb:0' and 'g+rw(x)' permission - to avoid problems running
container with arbitrary UID  
/usr/libexec/fix-permissions /etc/mongod.conf
${CONTAINER_SCRIPTS_PATH}/mongodb.conf.template \  
${HOME}  
  
VOLUME ["/var/lib/mongodb/data"]  
  
USER 184  

