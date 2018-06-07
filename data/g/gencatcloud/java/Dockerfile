FROM gencatcloud/alpine-glibc:3.6  
  
MAINTAINER suport.gencat@gencat.cat  
  
ENV JAVA_VERSION=7 \  
JAVA_UPDATE=80 \  
JAVA_PACKAGE=jdk \  
JAVA_MD5=6152f8a7561acf795ca4701daa10a965 \  
JAVA_JCE=unlimited \  
JAVA_JCE_SHA256=7a8d790e7bd9c2f82a83baddfae765797a4a56ea603c9150c87b7cdb7800194d
\  
JAVA_HOME="/usr/lib/jvm/default-jvm" \  
APP_DIR=/app  
  
RUN apk add \--no-cache \--virtual=build-dependencies wget ca-certificates
unzip && \  
cd "/tmp" && \  
wget "http://ftp.osuosl.org/pub/funtoo/distfiles/oracle-
java/${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
echo "${JAVA_MD5}
${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" > java.md5 &&
\  
md5sum -c java.md5 && \  
tar -xzf "${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" &&
\  
mkdir -p "/usr/lib/jvm" && \  
mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"/usr/lib/jvm/java-${JAVA_VERSION}-oracle" && \  
ln -s "java-${JAVA_VERSION}-oracle" "$JAVA_HOME" && \  
ln -s "$JAVA_HOME/bin/"* "/usr/bin/" && \  
rm -rf "$JAVA_HOME/"*src.zip && \  
rm -rf "$JAVA_HOME/lib/missioncontrol" \  
"$JAVA_HOME/lib/visualvm" \  
"$JAVA_HOME/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/plugin.jar" \  
"$JAVA_HOME/jre/lib/ext/jfxrt.jar" \  
"$JAVA_HOME/jre/bin/javaws" \  
"$JAVA_HOME/jre/lib/javaws.jar" \  
"$JAVA_HOME/jre/lib/desktop" \  
"$JAVA_HOME/jre/plugin" \  
"$JAVA_HOME/jre/lib/"deploy* \  
"$JAVA_HOME/jre/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/"*jfx* \  
"$JAVA_HOME/jre/lib/amd64/libdecora_sse.so" \  
"$JAVA_HOME/jre/lib/amd64/"libprism_*.so \  
"$JAVA_HOME/jre/lib/amd64/libfxplugins.so" \  
"$JAVA_HOME/jre/lib/amd64/libglass.so" \  
"$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so" \  
"$JAVA_HOME/jre/lib/amd64/"libjavafx*.so \  
"$JAVA_HOME/jre/lib/amd64/"libjfx*.so && \  
rm -rf "$JAVA_HOME/jre/bin/jjs" \  
"$JAVA_HOME/jre/bin/keytool" \  
"$JAVA_HOME/jre/bin/orbd" \  
"$JAVA_HOME/jre/bin/pack200" \  
"$JAVA_HOME/jre/bin/policytool" \  
"$JAVA_HOME/jre/bin/rmid" \  
"$JAVA_HOME/jre/bin/rmiregistry" \  
"$JAVA_HOME/jre/bin/servertool" \  
"$JAVA_HOME/jre/bin/tnameserv" \  
"$JAVA_HOME/jre/bin/unpack200" \  
"$JAVA_HOME/jre/lib/ext/nashorn.jar" \  
"$JAVA_HOME/jre/lib/jfr.jar" \  
"$JAVA_HOME/jre/lib/jfr" \  
"$JAVA_HOME/jre/lib/oblique-fonts" && \  
if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE
policy" >&2 && \  
wget "http://ftp.osuosl.org/pub/funtoo/distfiles/oracle-
java/UnlimitedJCEPolicyJDK${JAVA_VERSION}.zip" && \  
echo "${JAVA_JCE_SHA256} UnlimitedJCEPolicyJDK${JAVA_VERSION}.zip" > java-
jce.md5 && \  
sha256sum -c java-jce.md5 && \  
unzip -jo -d "${JAVA_HOME}/jre/lib/security"
"UnlimitedJCEPolicyJDK${JAVA_VERSION}.zip" && \  
rm "${JAVA_HOME}/jre/lib/security/README.txt";\  
fi && \  
apk del build-dependencies && \  
rm "/tmp/"*  
  
COPY fix-permissions.sh \  
wait-for-it.sh \  
run.sh /  
  
RUN chmod a+x /fix-permissions.sh /wait-for-it.sh /run.sh && \  
mkdir -p ${APP_DIR}  
RUN /fix-permissions.sh ${APP_DIR}  
# Define working directory.  
WORKDIR ${APP_DIR}  
  
CMD ["/run.sh"]

