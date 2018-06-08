FROM nuxeo/nuxeo:master  
MAINTAINER Damien Metzler <dmetzler@nuxeo.com>  
  
ENV BUILDER_VERSION 1.0  
ENV MAVEN_VERSION=3.5.2  
ENV STI_SCRIPTS_PATH=/usr/libexec/s2i  
  
LABEL io.k8s.description="Platform for building and running Nuxeo based
applications" \  
io.k8s.display-name="Nuxeo S2i 9.10" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,nuxeo,nuxeo93" \  
io.openshift.s2i.scripts-url="image://$STI_SCRIPTS_PATH" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
  
USER root  
  
# First install Maven  
RUN (curl -v
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
mkdir -p /home/nuxeo/.m2 && \  
mkdir -p /opt/s2i/destination && \  
# Then needed tools for Nuxeo build (ie npm & friends)  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
build-essential && \  
npm cache clean -f && \  
npm install -g n && \  
n stable && \  
ln -sf /usr/local/n/versions/node/8.0.0/bin/node /usr/bin/node && \  
npm install -g npm@latest && \  
npm install -g gulp grunt grunt-cli polymer-cli bower yo && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/s2i/destination && \  
chown -R 1000:0 /opt/s2i/destination && \  
chmod -R g+rwX /opt/s2i/destination && \  
chown -R 1000:0 /home/nuxeo && \  
chmod -R g+rwX /home/nuxeo && \  
mkdir -p /build/artifacts && \  
mkdir -p /build/marketplace && \  
chown -R 1000:0 /build/ && \  
chmod -R g+rwX /build/  
  
ADD ./contrib/settings.xml /home/nuxeo/.m2/  
ADD ./contrib/install.sh /build/install.sh  
  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
# This default user is created in the openshift/base-centos7 image  
USER 1000:0  
CMD ["/usr/libexec/s2i/usage"]  

