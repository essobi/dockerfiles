FROM debian:9-slim  
  
ENV SONARQUBE_VERSION=3.0.3.778 \  
FILE=sonar-scanner-cli \  
PLATFORM=linux \  
SONARQUBE_KEY=F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
KEYSERVER=ha.pool.sks-keyservers.net \  
BUILD_DEPS="gnupg wget unzip dirmngr" \  
DEPS="ca-certificates" \  
VERSION=1.0 \  
UID=1000 \  
GID=1000  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y ${BUILD_DEPS} ${DEPS}\  
&& wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip \  
&& wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip.asc \  
&& gpg --keyserver ${KEYSERVER} \--recv-keys ${SONARQUBE_KEY} \  
&& FINGERPRINT="$(LANG=C gpg --verify
${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip.asc
${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip 2>&1 \  
| sed -n "s#Primary key fingerprint: \\(.*\\)#\1#p" | tr -d '[:space:]')" \  
&& echo $FINGERPRINT \  
&& if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" &&
exit 1; fi \  
&& if [ "${FINGERPRINT}" != "${SONARQUBE_KEY}" ]; then echo "Warning! Wrong
GPG fingerprint!" && exit 1; fi \  
&& echo "Unzipping ${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip" \  
&& unzip ${FILE}-${SONARQUBE_VERSION}-${PLATFORM}.zip 2>&1 \  
&& ln -s /sonar-scanner-${SONARQUBE_VERSION}-${PLATFORM}/bin/sonar-scanner
/usr/sbin/sonar-scanner \  
&& apt-get remove -y ${BUILD_DEPS} \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /build  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
LABEL description="A docker image for scanning the code quality with sonarqube
cli" \  
nextcloud="Sonarqube CLI v${SONARQUBE_VERSION}" \  
maintainer="Motius <info@motius.de>"  

