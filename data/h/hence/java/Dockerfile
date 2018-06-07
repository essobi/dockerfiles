FROM hence/base:3.2-onbuild  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ONBUILD COPY help.txt $HENCE_PREFIX/help.txt  
ONBUILD COPY post-install.sh /tmp/post-install.sh  
  
ENV HENCE_APP_DIR=$HENCE_PREFIX/java \  
HENCE_APP_NAME=java \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.2  
ENV HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME \  
PATH=$HENCE_APP_DIR/bin:$PATH  
  
RUN apk add --update \  
nss \  
openjdk7-jre && \  
rm -rf /var/cache/apk/* && \  
find /usr/share/ca-certificates/mozilla/ -name *.crt -exec keytool -import
-trustcacerts \  
-keystore /usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts -storepass changeit -noprompt \  
-file {} -alias {} \; && \  
keytool -list -keystore /usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts
--storepass changeit  
  
# Expose reference to JAVA_HOME and  
# Adjust PATH to include all JDK related executables  
ENV JAVA_HOME=/usr/lib/jvm/java-1.7-openjdk \  
PATH=$JAVA_HOME/bin:$PATH  
  
COPY rootfs /  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
VOLUME ["/app", "$HENCE_APP_VOL_PREFIX/logs/java-general-logs",
"$HENCE_APP_VOL_PREFIX/logs/java-error-logs"]  
  
WORKDIR /app  

