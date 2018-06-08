# This image provides a base for building and running SpringBoot applications.  
# It builds using maven and runs the resulting artifacts on SpringBoot  
FROM openshift/base-centos7  
  
MAINTAINER Sarcouy <sarcouy@protonmail.com>  
  
EXPOSE 8080  
ENV MAVEN_VERSION=3.2.5 \  
JAVA="java-1.6.0-openjdk java-1.6.0-openjdk-devel" \  
JDK_VERSION=1.6 \  
SPRINGBOOT_HOME=/springboot \  
JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8 \  
POM_PATH=.  
  
LABEL io.k8s.description="Platform for building and running java applications
on Spring-Boot, Java-1.6" \  
io.k8s.display-name="SpringBoot, java-1.6" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder, Springboot, Java-1.6" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
  
# Install Maven, Java  
RUN INSTALL_PKGS="tar unzip bc which lsof $JAVA" && \  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
(curl -v
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
mkdir -p $HOME/.m2 && \  
mkdir -p $SPRINGBOOT_HOME \  
mkdir -p /opt/s2i/destination  
  
# Add s2i maven customizations  
ADD ./contrib/settings.xml $HOME/.m2/  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
RUN chown -R 1001:0 $SPRINGBOOT_HOME && chown -R 1001:0 $HOME && \  
chmod -R ug+rwx $SPRINGBOOT_HOME && \  
chmod -R g+rw /opt/s2i/destination  
  
USER 1001  
CMD $STI_SCRIPTS_PATH/usage  

