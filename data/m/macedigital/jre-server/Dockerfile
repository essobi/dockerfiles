# Base image for running JVM based applications  
FROM centos:7  
  
RUN VERSION=8 \  
&& UPDATE=121 \  
&& BUILD=13 \  
&& ARCHIVE=server-jre-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz \  
&& export TARGET=/usr/lib/jdk1."${VERSION}".0_"${UPDATE}" \  
&& DOWNLOAD_HASH="e9e7ea248e2c4826b92b3f075a80e441" \  
&& curl -SLO --header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${DOWNLOAD_HASH}"/"${ARCHIVE}"
\  
&& curl -SL
https://www.oracle.com/webfolder/s/digest/"${VERSION}"u"${UPDATE}"checksum.html
\  
| grep $(sha256sum "${ARCHIVE}" | cut -d ' ' -f1) \  
| grep -q "${ARCHIVE}" \  
&& tar -xf "${ARCHIVE}" -C $(dirname $TARGET) \  
&& mkdir -p /opt/java \  
&& mv "${TARGET}"/* /opt/java/ \  
&& rm -Rf "${ARCHIVE}" "${TARGET}" \  
&& chown root:root -R /opt/java \  
&& alternatives --install /usr/bin/java java "/opt/java/jre/bin/java" 1000  
  
ENV JAVA_HOME="/opt/java"  
ENV JAVA_OPTS="-Djavax.servlet.request.encoding=UTF-8 -Dfile.encoding=UTF-8
-Djava.awt.headless=true -Duser.timezone=UTC"  
ENV PATH "${JAVA_HOME}/jre/bin":$PATH  

