# Set the base image  
FROM openjdk:8-jre-alpine  
  
MAINTAINER Lightstreamer Server Development Team <support@lighstreamer.com>  
  
# Set environment variables to identify the right Lightstreamer version and
edition  
ENV LIGHSTREAMER_EDITION Allegro-Presto-Vivace  
ENV LIGHSTREAMER_VERSION 6_1_0_20170123  
ENV LIGHSTREAMER_URL_DOWNLOAD
http://www.lightstreamer.com/repo/distros/Lightstreamer_${LIGHSTREAMER_EDITION}_${LIGHSTREAMER_VERSION}.tar.gz  
  
# Set the temporary working dir  
WORKDIR /lightstreamer  
  
RUN set -x \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
tar \  
  
# Import Lighstreamer's public key  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
9B90BFD14309C7DA5EF58D7D4A8C08966F29B4D2 \  
  
# Download the package from the Lightstreamer site and replace the fictitious
jdk path with  
# the JAVA_HOME environment variable in the launch script file.  
&& wget -O Lightstreamer.tar.gz ${LIGHSTREAMER_URL_DOWNLOAD} \  
&& wget -O Lightstreamer.tar.gz.asc ${LIGHSTREAMER_URL_DOWNLOAD}.asc \  
&& gpg --batch --verify Lightstreamer.tar.gz.asc Lightstreamer.tar.gz \  
&& tar -xvf Lightstreamer.tar.gz --strip-components=1 \  
&& rm Lightstreamer.tar.gz Lightstreamer.tar.gz.asc \  
&& rm -r DOCS-SDKs \  
  
# Finally, adjust logging configuration to log only on standard output.  
&& sed -i -- 's/\/usr\/jdk1.8.0/$JAVA_HOME/' bin/unix-like/LS.sh \  
&& sed -i -e '123,$s/<appender-ref ref="LSDailyRolling" \/>/<appender-ref
ref="LSConsole" \/>/' \  
-e '/<appender-ref ref="LSDailyRolling" \/>/ d' conf/lightstreamer_log_conf.xml  
  
  
# Export TCP port 8080  
EXPOSE 8080  
# Set the final working dir  
WORKDIR /lightstreamer/bin/unix-like  
  
# Start the server  
CMD ["./LS.sh", "run"]  

