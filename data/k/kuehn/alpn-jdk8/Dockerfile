FROM qnib/alpn-rsyslog  
  
ARG JDK="8u111-b14"  
ENV LANG=C.UTF-8 \  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-8-oracle/bin/  
  
RUN apk add --update wget ca-certificates \  
&& export URL="http://download.oracle.com/otn-pub/java/jdk/$JDK/jdk-`echo
"$JDK" | sed 's@-[^-]*$@@g'`-linux-x64.tar.gz" \  
&& mkdir -p /usr/lib/jvm/java-8-oracle \  
&& cd /tmp \  
&& wget --quiet --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "$URL" \  
&& tar zxf /tmp/jdk-*-linux-x64.tar.gz -C /tmp/ \  
&& mv /tmp/jdk*/* /usr/lib/jvm/java-8-oracle/ \  
&& mkdir -p /usr/lib/jvm/java-8-oracle/jre/lib/security \  
&& rm -rf /var/cache/apk/* /tmp/* \  
${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/jre/plugin \  
${JAVA_HOME}/jre/bin/javaws \  
${JAVA_HOME}/jre/bin/jjs \  
${JAVA_HOME}/jre/bin/keytool \  
${JAVA_HOME}/jre/bin/orbd \  
${JAVA_HOME}/jre/bin/pack200 \  
${JAVA_HOME}/jre/bin/policytool \  
${JAVA_HOME}/jre/bin/rmid \  
${JAVA_HOME}/jre/bin/rmiregistry \  
${JAVA_HOME}/jre/bin/servertool \  
${JAVA_HOME}/jre/bin/tnameserv \  
${JAVA_HOME}/jre/bin/unpack200 \  
${JAVA_HOME}/jre/lib/javaws.jar \  
${JAVA_HOME}/jre/lib/deploy* \  
${JAVA_HOME}/jre/lib/desktop \  
${JAVA_HOME}/jre/lib/*javafx* \  
${JAVA_HOME}/jre/lib/*jfx* \  
${JAVA_HOME}/jre/lib/jfr* \  
${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/jre/lib/amd64/libprism_*.so \  
${JAVA_HOME}/jre/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/jre/lib/amd64/libglass.so \  
${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/jre/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/jre/lib/amd64/libjfx*.so \  
${JAVA_HOME}/jre/lib/ext/jfxrt.jar \  
${JAVA_HOME}/jre/lib/ext/nashorn.jar \  
${JAVA_HOME}/jre/lib/oblique-fonts \  
${JAVA_HOME}/jre/lib/plugin.jar \  
/tmp/* /var/cache/apk/* && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
RUN POLICY_URL="http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip" \  
&& POLICY_DIR="UnlimitedJCEPolicyJDK8" \  
&& wget --quiet --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
"$POLICY_URL" -O /tmp/policy.zip \  
&& cd /tmp \  
&& unzip /tmp/policy.zip \  
&& mv /tmp/$POLICY_DIR/*.jar /usr/lib/jvm/java-8-oracle/jre/lib/security/ \  
&& rm -rf /tmp/*  
  
WORKDIR /data  
  
RUN cd /tmp/ \  
&& wget -qO /usr/local/bin/go-github https://github.com/qnib/go-
github/releases/download/0.2.2/go-github_0.2.2_MuslLinux \  
&& chmod +x /usr/local/bin/go-github \  
&& echo "# download $(/usr/local/bin/go-github rLatestUrl --ghorg sgerrand
--ghrepo alpine-pkg-glibc --regex 'glibc-2.*.apk' |head -n1) "\  
&& wget -q $(/usr/local/bin/go-github rLatestUrl --ghorg sgerrand --ghrepo
alpine-pkg-glibc --regex "glibc-2.*.apk" |head -n1) \  
&& echo "# download $(/usr/local/bin/go-github rLatestUrl --ghorg sgerrand
--ghrepo alpine-pkg-glibc --regex 'glibc-bin-2.*.apk' |head -n1) "\  
&& wget -q $(/usr/local/bin/go-github rLatestUrl --ghorg sgerrand --ghrepo
alpine-pkg-glibc --regex "glibc-bin-2.*.apk" |head -n1) \  
&& apk add --no-cache --allow-untrusted glibc-*.apk \  
&& rm -rf /usr/local/bin/go-github /tmp/glibc-*  

