# fat-jar-webapp  
FROM openshift/base-centos7  
  
MAINTAINER Arkaprovo Bhattacharjee <arkaprovo.bhatatcharjee@sath.com>  
# HOME in base image is /opt/app-root/src  
#RUN mkdir /usr/libexec  
RUN mkdir /usr/libexec/s2i  
#RUN mkdir /usr/libexec/s2i/assemble  
# Install build tools on top of base image  
# Java jdk 8, Maven 3.5, Gradle 4.6  
RUN mkdir -p /usr/local/sti  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
mkdir -p /opt/openshift && \  
mkdir -p /opt/app-root/source && chmod -R a+rwX /opt/app-root/source && \  
mkdir -p /opt/s2i/destination && chmod -R a+rwX /opt/s2i/destination && \  
mkdir -p /opt/app-root/src && chmod -R a+rwX /opt/app-root/src  
  
ENV MAVEN_VERSION 3.5.3  
RUN (curl -0
http://www.eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
mv /usr/local/apache-maven-$MAVEN_VERSION /usr/local/maven && \  
ln -sf /usr/local/maven/bin/mvn /usr/local/bin/mvn && \  
mkdir -p $HOME/.m2 && chmod -R a+rwX $HOME/.m2  
  
ENV GRADLE_VERSION 4.6  
RUN curl -sL -0
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
/tmp/gradle-${GRADLE_VERSION}-bin.zip && \  
unzip /tmp/gradle-${GRADLE_VERSION}-bin.zip -d /usr/local/ && \  
rm /tmp/gradle-${GRADLE_VERSION}-bin.zip && \  
mv /usr/local/gradle-${GRADLE_VERSION} /usr/local/gradle && \  
ln -sf /usr/local/gradle/bin/gradle /usr/local/bin/gradle  
  
ENV PATH=/opt/maven/bin/:/opt/gradle/bin/:$PATH  
  
ENV BUILDER_VERSION 1.0  
# Set labels used in OpenShift to describe the builder image  
LABEL io.k8s.description="Platform for building Java (fatjar) applications
with maven or gradle" \  
io.k8s.display-name="Java S2I-FatJar builder 1.0" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,maven-3,gradle-4,java,microservices,fatjar"  
  
# TODO (optional): Copy the builder files into /opt/openshift  
# COPY ./<builder_folder>/ /opt/openshift/  
# COPY Additional files,configurations that we want to ship by default, like a
default setting.xml  
COPY ./contrib/settings.xml $HOME/.m2/  
  
# TODO (optional): Copy the builder files into /opt/app-root  
# COPY ./<builder_folder>/ /opt/app-root/  
# Copy the S2I scripts to /usr/local/sti, since openshift/base-centos7 image  
# sets io.openshift.s2i.scripts-url label that way, or update that label  
LABEL io.openshift.s2i.scripts-url=image:///usr/local/sti  
COPY ./s2i/bin/ /usr/local/sti  
RUN chmod +x /usr/local/sti/*  
# the root user and make the content of /opt/app-root owned by user 1001  
# RUN chown -R 1001:1001 /opt/app-root  
RUN chown -R 1001:1001 /opt/openshift  
# This default user is created in the openshift/base-centos7 image  
USER 1001  
#USER root  
# Set the default port for applications built using this image  
EXPOSE 8080  
# TODO: Set the default CMD for the image  
CMD ["echo","please refer usage"]  

