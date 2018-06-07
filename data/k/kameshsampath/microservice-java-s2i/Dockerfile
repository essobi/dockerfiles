FROM openshift/base-centos7  
  
MAINTAINER Kamesh Sampath, kamesh.sampath@hotmail.com  
  
ENV JAVA_APP_DIR=/app \  
JAVA_DATA_DIR=/app/data \  
MAVEN_VERSION=3.3.9 \  
JAVA_VERSION=1.8.0  
  
LABEL io.k8s.description="Platform for building and running springboot,
wildfly-swarm microservice applications" \  
io.k8s.display-name="Microservice s2i" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,msa,springboot,wildfly-swarm" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
(curl -v
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
mkdir -p $HOME/.m2 && \  
mkdir -p /app/data && \  
mkdir -p /opt/s2i/destination && \  
mkdir -p /app/data && \  
mkdir -p $HOME/.m2  
  
COPY ./s2i/bin $STI_SCRIPTS_PATH  
ADD ./m2/settings.xml $HOME/.m2  
ADD ./README.md $STI_SCRIPTS_PATH/usage.txt  
  
RUN chown -R 1001:0 $HOME && \  
chmod -R g+rwx $STI_SCRIPTS_PATH && \  
chmod -R g+rw /opt/s2i/destination  
  
USER 1001  
  
CMD $STI_SCRIPTS_PATH/usage

