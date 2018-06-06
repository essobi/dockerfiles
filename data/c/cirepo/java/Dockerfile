# ${DOCKER_REGISTRY}/java:oracle-8u171-jdk-alpine  
#  
# The main caveat to note is that it does use musl libc instead of glibc and
friends,  
# so certain software might run into issues depending on the depth of their
libc requirements.  
# However, most software doesn't have an issue with this,  
# so this variant is usually a very safe choice.  
#  
  
  
  
FROM alpine:3.7  
  
  
  
  
  
MAINTAINER haolun  
  
ARG build_fileserver  
ENV ARIA2C_DOWNLOAD aria2c --file-allocation=none -c -x 10 -s 10 -m 0
\--console-log-level=notice --log-level=notice --summary-interval=0  
  
ENV JDK8_HOME /usr/lib/jvm/java-8-oracle  
# Smaller Java images with Alpine Linux  
# see: https://developer.atlassian.com/blog/2015/08/minimal-java-docker-
containers/  
# http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz  
  
  
RUN set -ex \  
&& echo ===== Install tools ===== \  
&& echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main" >
/etc/apk/repositories \  
&& echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/community" >>
/etc/apk/repositories \  
&& echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/testing/" >>
/etc/apk/repositories \  
&& apk add --update --upgrade apk-tools \  
&& apk upgrade --update \  
&& apk add aria2 bash binutils ca-certificates curl git libstdc++ openssh tar
unzip wget xz \  
&& echo ===== Set locale ===== \  
&& apk add font-adobe-100dpi tzdata \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& apk del tzdata \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& echo "UTC+8:00" > /etc/TZ \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
&& echo ===== Install waitforit ===== \  
&& ${ARIA2C_DOWNLOAD} -d /usr/bin -o "waitforit"
"http://o9wbz99tz.bkt.clouddn.com/maxcnunes/waitforit/releases/download/v2.2.0/waitforit-
linux_amd64" \  
&& chmod 755 /usr/bin/waitforit \  
&& echo ===== Install glibc ===== \  
&& GLIBC_VERSION="2.23-r3" \  
&& ${ARIA2C_DOWNLOAD} -d /tmp -o "glibc-${GLIBC_VERSION}.apk"
"http://o9wbz99tz.bkt.clouddn.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk \  
&& echo ===== Install JDK8 ===== \  
&& JAVA_VERSION_MAJOR=8 \  
&& JAVA_VERSION_MINOR=171 \  
&& JAVA_VERSION_BUILD=11 \  
&& JAVA_PACKAGE=jdk \  
&& JAVA_PACKAGE_DIGEST=512cd62ec5174c3487ac17c61aaa89e8 \  
&& if [ -z "${build_fileserver}" ]; then
build_fileserver="http://download.oracle.com"; fi \  
&& mkdir -p $(dirname ${JDK8_HOME}) \  
&& curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
${build_fileserver}/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE_DIGEST}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C $(dirname ${JDK8_HOME}) \  
&& mv $(dirname
${JDK8_HOME})/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JDK8_HOME}
\  
&& mkdir -p
/Library/Java/JavaVirtualMachines/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}.jdk/Contents
\  
&& ln -s ${JDK8_HOME}
/Library/Java/JavaVirtualMachines/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}.jdk/Contents/Home
\  
&& rm -rf ${JDK8_HOME}/*src.zip \  
${JDK8_HOME}/lib/missioncontrol \  
${JDK8_HOME}/lib/visualvm \  
${JDK8_HOME}/lib/*javafx* \  
${JDK8_HOME}/jre/lib/plugin.jar \  
${JDK8_HOME}/jre/lib/ext/jfxrt.jar \  
${JDK8_HOME}/jre/bin/javaws \  
${JDK8_HOME}/jre/lib/javaws.jar \  
${JDK8_HOME}/jre/lib/desktop \  
${JDK8_HOME}/jre/plugin \  
${JDK8_HOME}/jre/lib/deploy* \  
${JDK8_HOME}/jre/lib/*javafx* \  
${JDK8_HOME}/jre/lib/*jfx* \  
${JDK8_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JDK8_HOME}/jre/lib/amd64/libprism_*.so \  
${JDK8_HOME}/jre/lib/amd64/libfxplugins.so \  
${JDK8_HOME}/jre/lib/amd64/libglass.so \  
${JDK8_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JDK8_HOME}/jre/lib/amd64/libjavafx*.so \  
${JDK8_HOME}/jre/lib/amd64/libjfx*.so \  
&& POLICY_DIR="UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}" \  
&& curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" \  
${build_fileserver}/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip >
policy.zip \  
&& unzip policy.zip \  
&& cp -f ${POLICY_DIR}/US_export_policy.jar
${JDK8_HOME}/jre/lib/security/US_export_policy.jar \  
&& cp -f ${POLICY_DIR}/local_policy.jar
${JDK8_HOME}/jre/lib/security/local_policy.jar \  
&& rm -rf ${POLICY_DIR} \  
&& rm -f policy.zip \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
## Install OpenJDK 8 (latest edition)  
#RUN apt-get -q update &&\  
# DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="
--force-confnew" --no-install-recommends openjdk-8-jdk-headless &&\  
# apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
# Install agents  
COPY docker/ejstatd-1.0.0.jar /opt/ejstatd/ejstatd-1.0.0.jar  
# Need libstdc++.so.6 in libstdc++  
# Could not find agent library /opt/jprofiler/bin/linux-x64/libjprofilerti.so
in absolute path, with error: libstdc++.so.6: cannot open shared object file:
No such file or directory  
COPY docker/jprofiler/bin/linux-x64/libattach.so
/opt/jprofiler/bin/linux-x64/libattach.so  
COPY docker/jprofiler/bin/linux-x64/libjprofilerti.so
/opt/jprofiler/bin/linux-x64/libjprofilerti.so  
COPY docker/java_debug_monitor_profiler.sh /opt/java_debug_monitor_profiler.sh  
  
# Set environment  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
ENV JAVA_HOME ${JDK8_HOME}  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
  
ENV LD_LIBRARY_PATH /lib:/usr/lib:/usr/local/lib  
  
ENV JAVA_OPTS -Duser.language=zh -Duser.region=CN -Dfile.encoding=UTF-8
-Duser.timezone=Asia/Shanghai  

