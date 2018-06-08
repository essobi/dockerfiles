# Set the base image  
FROM openjdk:8-jre-alpine  
  
LABEL maintainer="Lightstreamer Server Development Team
<support@lightstreamer.com>"  
  
# Set environment variables to identify the right Lightstreamer version  
ENV LIGHTSTREAMER_VERSION 7_0_0_20180228  
ENV LIGHTSTREAMER_URL_DOWNLOAD
http://www.lightstreamer.com/repo/distros/Lightstreamer_${LIGHTSTREAMER_VERSION}.tar.gz  
  
# Set the temporary working dir  
WORKDIR /lightstreamer  
  
# Install the required packages  
RUN set -ex; \  
apk add --no-cache --virtual .deps \  
gnupg \  
tar \  
curl \  
  
# Import Lighstreamer's public key  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
9B90BFD14309C7DA5EF58D7D4A8C08966F29B4D2 \  
  
# Download the distribution from the Lightstreamer site, verify the signature,
and unpack  
&& set -ex; \  
curl -fSL -o Lightstreamer.tar.gz ${LIGHTSTREAMER_URL_DOWNLOAD} \  
&& curl -fSL -o Lightstreamer.tar.gz.asc ${LIGHTSTREAMER_URL_DOWNLOAD}.asc \  
&& gpg --batch --verify Lightstreamer.tar.gz.asc Lightstreamer.tar.gz \  
&& tar -xvf Lightstreamer.tar.gz --strip-components=1 \  
  
# Replace the fictitious jdk path with the JAVA_HOME environment variable in
the launch script file  
&& sed -i -- 's/\/usr\/jdk1.8.0/$JAVA_HOME/' bin/unix-like/LS.sh \  
  
# Adjust the logging configuration in order to log only on standard output.  
&& sed -i -e '123,$s/<appender-ref ref="LSDailyRolling" \/>/<appender-ref
ref="LSConsole" \/>/' \  
-e '/<appender-ref ref="LSDailyRolling" \/>/ d' conf/lightstreamer_log_conf.xml \  
  
# Finally, remove no longer needed packages and files  
&& apk del .deps \  
&& rm Lightstreamer.tar.gz Lightstreamer.tar.gz.asc  
  
# Export TCP port 8080  
EXPOSE 8080  
# Set the final working dir  
WORKDIR /lightstreamer/bin/unix-like  
  
# Start the server  
CMD ["./LS.sh", "run"]  

