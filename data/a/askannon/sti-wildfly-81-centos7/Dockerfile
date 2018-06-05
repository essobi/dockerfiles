# This image provides a base for building and running WildFly applications.  
# It builds using maven and runs the resulting artifacts on WildFly 8.1.  
FROM alpine:3.3  
MAINTAINER Askannon <askannon@flexarc.com>  
  
EXPOSE 8080  
ENV STI_SCRIPTS_PATH="/usr/local/s2i" \  
WILDFLY_VERSION=8.1 \  
WILDFLY_VERSION_BIN=8.1.0.Final \  
MAVEN_VERSION=3.3.3 \  
PATH=$PATH:"/usr/local/s2i" \  
JAVA_HOME=/usr/lib/jvm/default-jvm \  
HOME="/wildfly"  
LABEL io.k8s.description="Platform for building and running JEE applications
on WildFly 8.1" \  
io.k8s.display-name="WildFly 8.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,wildfly,wildfly81" \  
io.openshift.s2i.destination="/opt/s2i/destination" \  
io.openshift.s2i.scripts-url="image:///usr/local/s2i"  
  
# Install Maven, Wildfly 8  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
bash \  
curl \  
openjdk8 \  
ngrep \  
tcpdump \  
lsof \  
tar \  
bc \  
unzip \  
ca-certificates && \  
rm /var/cache/apk/*  
  
# Update java keystore since alpine doesn't ship with them and thus SSL
connections cause issues  
RUN find /usr/share/ca-certificates/mozilla/ -name "*.crt" -exec keytool
-import -trustcacerts \  
-keystore ${JAVA_HOME}/jre/lib/security/cacerts -storepass changeit -noprompt \  
-file {} -alias {} \; && \  
keytool -list -keystore ${JAVA_HOME}/jre/lib/security/cacerts --storepass
changeit  
  
# Install Maven  
RUN (curl -0
http://www.us.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
mkdir -p /wildfly && \  
(curl -0
http://download.jboss.org/wildfly/$WILDFLY_VERSION_BIN/wildfly-$WILDFLY_VERSION_BIN.tar.gz
| tar -zx --strip-components=1 -C /wildfly) && \  
mkdir -p /opt/s2i/destination  
  
# Add sti wildfly customizations  
ADD ./contrib/wfmodules/ /wildfly/modules/  
ADD ./contrib/wfbin/ /wildfly/bin/  
ADD ./contrib/wfcfg/ /wildfly/standalone/configuration/  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
# Add a user to run our stuff  
RUN adduser -D -u 1001 -h ${HOME} -G root -s /sbin/nologin -g "Default
Application User" default  
  
RUN chown -R 1001:0 /wildfly && \  
chmod -R ug+rw /wildfly && \  
chmod -R g+rw /opt/s2i/destination  
  
USER 1001  
CMD $STI_SCRIPTS_PATH/usage  

