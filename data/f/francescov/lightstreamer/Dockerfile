# Set the base image  
FROM openjdk:8u131-jre-alpine  
  
# Set environment variables to identify the right Lightstreamer version and
edition  
ENV LIGHSTREAMER_VERSION=6_1_0_20170123  
ENV LIGHSTREAMER_EDITION Allegro-Presto-Vivace  
ENV LIGHSTREAMER_URL_DOWNLOAD
http://www.lightstreamer.com/repo/distros/Lightstreamer_${LIGHSTREAMER_EDITION}_${LIGHSTREAMER_VERSION}.tar.gz  
  
# Set the temporary working dir  
WORKDIR /lightstreamer  
  
# Download the package from the Lightstreamer site and replace the fictitious
jdk path with  
# the JAVA_HOME environment variable in the launch script file.  
# Finally, adjust logging configuration to log only on standard output.  
RUN set -x \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
tar \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
9B90BFD14309C7DA5EF58D7D4A8C08966F29B4D2 \  
&& wget -O Lightstreamer.tar.gz ${LIGHSTREAMER_URL_DOWNLOAD} \  
&& wget -O Lightstreamer.tar.gz.asc ${LIGHSTREAMER_URL_DOWNLOAD}.asc \  
&& gpg --batch --verify Lightstreamer.tar.gz.asc Lightstreamer.tar.gz \  
&& tar -xvf Lightstreamer.tar.gz --strip-components=1 \  
&& rm Lightstreamer.tar.gz Lightstreamer.tar.gz.asc \  
&& rm -rf adapters/* bin/unix-like/install bin/windows conf/mpn DOCS-SDKs
lib/mpn/* logs/* pages/* CHANGELOG.HTML *.TXT \  
&& sed -i -- 's/\/usr\/jdk1.8.0/$JAVA_HOME/' bin/unix-like/LS.sh \  
&& apk del gnupg tar  
  
# Set the final working dir  
WORKDIR /lightstreamer/bin/unix-like  
  
# Start the server  
CMD ["./LS.sh", "run"]  

