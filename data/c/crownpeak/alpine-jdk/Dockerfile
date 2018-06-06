##################################################################################################  
# Image: crownpeak/alpine-jdk:8  
# Maintained by: CrownPeak Advanced Solutions Group <asg@crownpeak.com>
<mark.kelly@crownpeak.com>  
##################################################################################################  
  
FROM crownpeak/alpine-glibc:2.23-r3  
MAINTAINER Crownpeak Advanced Solutions Group <asg@crownpeak.com>
<mark.kelly@crownpeak.com>  
  
ENV CROWNPEAK_DIR="/usr/local/crownpeak" \  
JAVA_VERSION=8 \  
JAVA_UPDATE=102 \  
JAVA_BUILD=14 \  
JAVA_TYPE="server-jre"  
  
# Install wget & ca-certs so we can download the server JRE  
# Work within the CROWNPEAK_DIR to remove the need to move files around  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \  
mkdir -p "${CROWNPEAK_DIR}" && \  
cd "${CROWNPEAK_DIR}" && \  
# wget file allows us to dynamically change the version via variables.  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_TYPE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
&& \  
tar -xzf "${JAVA_TYPE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
ln -s "${CROWNPEAK_DIR}/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"${CROWNPEAK_DIR}/server-jre-${JAVA_VERSION}" && \  
apk del build-dependencies && \  
# Remove the tar.gz  
rm -f "${JAVA_TYPE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
cd "${CROWNPEAK_DIR}/${JAVA_TYPE}-${JAVA_VERSION}" && \  
# Remove unnecessary files from the archive  
rm -Rf \  
COPYRIGHT \  
LICENSE \  
README.html \  
THIRDPARTYLICENSEREADME-JAVAFX.txt \  
THIRDPARTYLICENSEREADME.txt \  
release \  
src.zip \  
man/  
  
# Update PATH to include Java/bin  
ENV PATH="${CROWNPEAK_DIR}/${JAVA_TYPE}-${JAVA_VERSION}/bin:${PATH}"  
  
# Should we only provide an entry point to Java?  
CMD ["/bin/sh"]  

