FROM docker.io/debian:jessie  
MAINTAINER Martin W. Kirst "x.nitram509@gmail.com"  
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://github.com/nitram509/docker-debian-
oraclejdk8-maven-cmake-gcc-gnueabihf" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/nitram509/docker-debian-
oraclejdk8-maven-cmake-gcc-gnueabihf.git"  
  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=74 \  
JAVA_BUILD=02 \  
JAVA_SHA256_SUM="0bfd5d79f776d448efc64cb47075a52618ef76aabb31fde21c5c1018683cdddd"
\  
JAVA_HOME="/usr/lib/jvm/default-jvm" \  
MAVEN_HOME="/usr/share/maven" \  
MAVEN_VERSION="3.3.9" \  
MAVEN_MD5_SUM="516923b3955b6035ba6b0a5b031fbd8b" \  
EMDEBIAN_ARCHIVE_KEY="emdebian-toolchain-archive.key" \  
EMDEBIAN_ARCHIVE_KEY_FINGERPRINT="Keyfingerprint=084C6C6F39159EDB67969AA87DE089671804772E"  
  
RUN cd "/tmp" && \  
apt-get update && \  
apt-get -y install wget pgpgpg && \  
echo "deb http://emdebian.org/tools/debian/ jessie main" >
"/etc/apt/sources.list.d/crosstools.list" && \  
wget -qO- "http://emdebian.org/tools/debian/${EMDEBIAN_ARCHIVE_KEY}" >
"${EMDEBIAN_ARCHIVE_KEY}" && \  
export archive_key_fingerprint=$(gpg -a --with-fingerprint
"${EMDEBIAN_ARCHIVE_KEY}" | tail -n 1 | sed 's/\s*//g') && \  
if [ "${archive_key_fingerprint}" != "${EMDEBIAN_ARCHIVE_KEY_FINGERPRINT}" ];
then echo "ERROR, invalid debian archive key fingerprint. Please, verify the
key."; exit 1; fi && \  
apt-key add "$EMDEBIAN_ARCHIVE_KEY" && \  
dpkg --add-architecture armhf && \  
apt-get update && \  
apt-get -y install git gcc-4.8 g++-4.8 make cmake && \  
apt-get -y install crossbuild-essential-armhf binutils-arm-linux-gnueabihf &&
\  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
&& \  
echo "${JAVA_SHA256_SUM}"
"jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" | sha256sum -c - && \  
tar -xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
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
wget -q -O "maven-${MAVEN_VERSION}-bin.tar.gz"
"http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz" && \  
echo "${MAVEN_MD5_SUM}" "maven-${MAVEN_VERSION}-bin.tar.gz" | md5sum -c - && \  
tar -xvzf "maven-${MAVEN_VERSION}-bin.tar.gz" && \  
mv "/tmp/apache-maven-${MAVEN_VERSION}" /usr/share/maven && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \  
apt-get -y autoremove wget pgpgpg && \  
apt-get -y clean && \  
rm -rf "/tmp/"* \  
"/var/cache/apt" \  
"/usr/share/man" \  
"/usr/share/doc" \  
"/usr/share/doc-base" \  
"/usr/share/info/*" \  
"/root/.gnupg"  

