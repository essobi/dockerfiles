# Dockerizing a base images with:  
#  
# - Ubuntu 14.04  
# - Oracle JDK 8  
#  
# Build: docker build -t exoplatform/base-jdk:jdk8 .  
#  
# Run: docker run -ti exoplatform/base-jdk:jdk8 bash  
FROM phusion/baseimage:0.9.18  
LABEL maintainer="eXo Platform <docker@exoplatform.com>"  
  
ENV TERM xterm  
  
ENV JDK_VERSION_MAJOR 8  
ENV JDK_VERSION_UPDATE 151  
ENV JDK_VERSION_BUILD b12  
ENV JDK_VERSION_HASH e758a0de34e24606bca991d704f6dcbf  
  
  
ENV JDK_VERSION ${JDK_VERSION_MAJOR}u${JDK_VERSION_UPDATE}  
ENV JDK_VERSION_DOT 1.${JDK_VERSION_MAJOR}.0  
ENV JDK_VERSION_DOT_UPDATE ${JDK_VERSION_DOT}_${JDK_VERSION_UPDATE}  
ENV JDK_DOWNLOAD http://download.oracle.com/otn-
pub/java/jdk/${JDK_VERSION}-${JDK_VERSION_BUILD}/${JDK_VERSION_HASH}/jdk-${JDK_VERSION}-linux-x64.tar.gz  
  
# Cleanup the base image from useless things  
RUN rm -rf /etc/service/sshd/  
  
# Install some useful or needed tools  
ENV DEBIAN_FRONTEND noninteractive  
# --force-confold: do not modify the current configuration file, the new
version is installed with a .dpkg-dist suffix. With this option alone, even
configuration  
# files that you have not modified are left untouched. You need to combine it
with  
# --force-confdef to let dpkg overwrite configuration files that you have not
modified.  
ENV _APT_OPTIONS -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--
force-confold"  
RUN apt-get -qq update \  
&& apt-get -qq -y upgrade ${_APT_OPTIONS} \  
&& apt-get -qq -y install ${_APT_OPTIONS} \  
wget \  
curl \  
expect \  
htop \  
unzip \  
&& apt-get -qq -y autoremove \  
&& apt-get -qq -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create needed directories  
ENV DOWNLOAD_DIR /srv/downloads  
RUN mkdir -p "${DOWNLOAD_DIR}"  
  
# Add some aliases  
RUN echo "alias ll='ls -al --color'" > /etc/profile.d/aliases.sh  
  
# Configure htop for root user  
RUN mkdir -p /root/.config/htop/ && chmod -R 700 /root/.config/htop/  
ADD conf/htoprc.conf /root/.config/htop/htoprc  
  
# Install Oracle Java 8 SDK  
ENV JVM_DIR /usr/lib/jvm  
RUN mkdir -p "${JVM_DIR}"  
  
RUN wget -q --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
-O "${DOWNLOAD_DIR}/jdk-${JDK_VERSION}-linux-x64.tar.gz" "${JDK_DOWNLOAD}" \  
&& cd "${JVM_DIR}" \  
&& tar --no-same-owner -xzf
"${DOWNLOAD_DIR}/jdk-${JDK_VERSION}-linux-x64.tar.gz" \  
&& rm -f "${DOWNLOAD_DIR}/jdk-${JDK_VERSION}-linux-x64.tar.gz" \  
&& mv "${JVM_DIR}/jdk${JDK_VERSION_DOT_UPDATE}"
"${JVM_DIR}/java-${JDK_VERSION_DOT_UPDATE}-oracle-x64" \  
&& ln -s "${JVM_DIR}/java-${JDK_VERSION_DOT_UPDATE}-oracle-x64"
"${JVM_DIR}/java-${JDK_VERSION_DOT}-oracle-x64"  
  
ADD java-${JDK_VERSION_DOT}-oracle-x64.jinfo
${JVM_DIR}/.java-${JDK_VERSION_DOT}-oracle-x64.jinfo  
RUN cat "${JVM_DIR}/.java-${JDK_VERSION_DOT}-oracle-x64.jinfo" | grep -E
'^(jre|jdk|hl)' | awk '{print "/usr/bin/" $2 " " $2 " " $3 " 30 \n"}' | xargs
-t -n4 sudo update-alternatives --install  
ENV JAVA_HOME ${JVM_DIR}/java-${JDK_VERSION_DOT}-oracle-x64  

