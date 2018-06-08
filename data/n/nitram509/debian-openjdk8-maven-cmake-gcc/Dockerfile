FROM docker.io/debian:jessie  
MAINTAINER Martin W. Kirst "x.nitram509@gmail.com"  
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://github.com/nitram509/docker-debian-
openjdk8-maven-cmake-gcc" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/nitram509/docker-debian-
openjdk8-maven-cmake-gcc.git"  
  
ENV ZULU_BASE_NAME="zulu8.17.0.3-jdk8.0.102-linux_x64"  
ENV ZULU_DOWNLOAD_URL="http://cdn.azul.com/zulu/bin/${ZULU_BASE_NAME}.tar.gz"
\  
JAVA_HOME="/usr/local/${ZULU_BASE_NAME}" \  
ZULU_CHECKSUM_MD5="abd8b70fa1a743f74c43d21f0a9bea43" \  
MAVEN_HOME="/usr/share/maven" \  
MAVEN_VERSION="3.3.9"  
  
RUN cd "/tmp" && \  
apt-get update && \  
# -----------------------------  
echo "installing basic tools ..." && \  
apt-get -y install wget && \  
apt-get -y install git && \  
apt-get -y install gcc-4.8 && \  
apt-get -y install g++-4.8 && \  
apt-get -y install make && \  
apt-get -y install cmake && \  
# -----------------------------  
echo "setup GCC-4.8 links ..." && \  
rm -rf "/usr/bin/cpp" \  
"/usr/bin/gcc" \  
"/usr/bin/g++" \  
"/usr/bin/gcc-ar" \  
"/usr/bin/gcc-nm" \  
"/usr/bin/gcc-ranlib" \  
"/usr/bin/gcov" \  
"/usr/bin/x86_64-linux-gnu-cpp" \  
"/usr/bin/x86_64-linux-gnu-gcc" \  
"/usr/bin/x86_64-linux-gnu-g++" \  
"/usr/bin/x86_64-linux-gnu-gcc-ar" \  
"/usr/bin/x86_64-linux-gnu-gcc-nm" \  
"/usr/bin/x86_64-linux-gnu-gcc-ranlib" \  
"/usr/bin/x86_64-linux-gnu-gcov" && \  
ln -s /usr/bin/cpp-4.8 /usr/bin/cpp && \  
ln -s /usr/bin/gcc-4.8 /usr/bin/gcc && \  
ln -s "/usr/bin/g++-4.8" "/usr/bin/g++" && \  
ln -s /usr/bin/gcc-ar-4.8 /usr/bin/gcc-ar && \  
ln -s /usr/bin/gcc-nm-4.8 /usr/bin/gcc-nm && \  
ln -s /usr/bin/gcc-ranlib-4.8 /usr/bin/gcc-ranlib && \  
ln -s /usr/bin/gcov-4.8 /usr/bin/gcov && \  
ln -s /usr/bin/x86_64-linux-gnu-cpp-4.8 /usr/bin/x86_64-linux-gnu-cpp && \  
ln -s /usr/bin/x86_64-linux-gnu-gcc-4.8 /usr/bin/x86_64-linux-gnu-gcc && \  
ln -s "/usr/bin/x86_64-linux-gnu-g++-4.8" "/usr/bin/x86_64-linux-gnu-g++" && \  
ln -s /usr/bin/x86_64-linux-gnu-gcc-ar-4.8 /usr/bin/x86_64-linux-gnu-gcc-ar &&
\  
ln -s /usr/bin/x86_64-linux-gnu-gcc-nm-4.8 /usr/bin/x86_64-linux-gnu-gcc-nm &&
\  
ln -s /usr/bin/x86_64-linux-gnu-gcc-ranlib-4.8 /usr/bin/x86_64-linux-gnu-gcc-
ranlib && \  
ln -s /usr/bin/x86_64-linux-gnu-gcov-4.8 /usr/bin/x86_64-linux-gnu-gcov && \  
# -----------------------------  
echo "installing Maven ..." && \  
wget -q
"http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" -O - | tar xvzf - && \  
mv apache-maven-$MAVEN_VERSION /usr/share/maven && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \  
# -----------------------------  
echo "installing OpenJDK ..." && \  
wget -q "${ZULU_DOWNLOAD_URL}" -O "/tmp/${ZULU_BASE_NAME}.tar.gz" && \  
echo "${ZULU_CHECKSUM_MD5} /tmp/${ZULU_BASE_NAME}.tar.gz" | md5sum -c - &&\  
cd "/usr/local" && \  
tar -xzf "/tmp/${ZULU_BASE_NAME}.tar.gz" && \  
ln -s "$JAVA_HOME/bin/"* "/usr/bin/" && \  
cd "/tmp" && \  
# -----------------------------  
echo "cleanup unused Java files ..." && \  
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
# -----------------------------  
echo "cleanup unused files ..." && \  
apt-get -y autoremove wget && \  
apt-get -y clean && \  
rm -rf "/tmp/"* \  
"/var/cache/apt" \  
"/usr/share/man" \  
"/usr/share/doc" \  
"/usr/share/doc-base" \  
"/usr/share/info/*" \  
"/root/.gnupg" \  

