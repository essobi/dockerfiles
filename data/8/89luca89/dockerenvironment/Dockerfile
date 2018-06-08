FROM frolvlad/alpine-glibc:alpine-3.6  
  
LABEL Authors="Luca Di Maio <luca.dimaio@ttss.ch>"  
LABEL Version="1.0"  
# Install my Utils  
RUN apk upgrade --no-cache && \  
apk add --no-cache bash && \  
apk add --no-cache tg && \  
apk add --no-cache git && \  
apk add --no-cache weechat && \  
apk add --no-cache weechat-perl && \  
apk add --no-cache weechat-python && \  
apk add --no-cache tmux && \  
apk add --no-cache mutt && \  
apk add --no-cache python2 && \  
apk add --no-cache python3 && \  
apk add --no-cache speedtest-cli && \  
apk add --no-cache py2-pip && \  
apk add --no-cache py3-pip && \  
apk add --no-cache php7 && \  
pip install websocket-client  
  
# Install java-jdk8  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=141 \  
JAVA_BUILD=15 \  
JAVA_PATH=336fa29ff2bb4ef291e347e091f7f4a7 \  
JAVA_HOME="/usr/lib/jvm/default-jvm"  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates unzip
&& \  
cd "/tmp" && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_PATH}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
&& \  
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
wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip" && \  
unzip -jo -d "${JAVA_HOME}/jre/lib/security" "jce_policy-${JAVA_VERSION}.zip"
&& \  
rm "${JAVA_HOME}/jre/lib/security/README.txt" && \  
apk del build-dependencies && \  
rm "/tmp/"*  
  
# Install Scala  
ENV SCALA_VERSION=2.12.1 \  
SCALA_HOME=/usr/share/scala  
RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
apk add --no-cache bash && \  
cd "/tmp" && \  
wget
"https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz"
&& \  
tar xzf "scala-${SCALA_VERSION}.tgz" && \  
mkdir "${SCALA_HOME}" && \  
rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \  
mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib"
"${SCALA_HOME}" && \  
ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \  
apk del .build-dependencies && \  
rm -rf "/tmp/"*  
  
# Install kotlin  
ENV KOTLIN_VERSION=1.0.4 \  
KOTLIN_HOME=/usr/share/kotlin  
  
RUN apk add --update bash && \  
apk add --virtual=build-dependencies wget ca-certificates && \  
cd /tmp && \  
wget
"https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-
compiler-${KOTLIN_VERSION}.zip" && \  
unzip "kotlin-compiler-${KOTLIN_VERSION}.zip" && \  
mkdir "${KOTLIN_HOME}" && \  
rm "/tmp/kotlinc/bin/"*.bat && \  
mv "/tmp/kotlinc/bin" "/tmp/kotlinc/lib" "${KOTLIN_HOME}" && \  
ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/" && \  
apk del build-dependencies && \  
rm -rf /tmp/* /var/cache/apk/*  
  
COPY run.sh /usr/local/bin/run.sh  
COPY assh /usr/local/bin/assh  
  
ENTRYPOINT ["run.sh"]

