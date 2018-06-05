FROM boky/java8  
  
ENV ANT_VERSION=1.9.7  
ENV MAX_FD="maximum"  
  
ENV ANT_HOME=/usr/lib/ant/default  
ENV ANT=$ANT_HOME/bin  
ENV JAVA_HOME="/usr/lib/jvm/default-jvm"  
ENV JAVA=$JAVA_HOME/bin/java  
ENV PATH $PATH:$JAVA_HOME:$JAVA_HOME/bin:$ANT  
  
RUN \  
apk add \--no-cache \--virtual=build-dependencies \--update curl ca-
certificates tar readline build-base && \  
cd /tmp && \  
echo "Downloading Ant ${ANT_VERSION}..." && \  
curl \--retry 5 \--max-time 120 \--connect-timeout 5 -fsSL -O
http://mirror.vorboss.net/apache/ant/binaries/apache-
ant-${ANT_VERSION}-bin.zip && \  
unzip -q apache*zip && \  
rm apache*zip && \  
mkdir -p /usr/lib/ant && \  
mv /tmp/apache-ant* /usr/lib/ant/${ANT_VERSION} && \  
ln -s /usr/lib/ant/${ANT_VERSION} ${ANT_HOME} && \  
echo "*** ANT INSTALLED ***" && \  
apk add \--no-cache \--virtual=build-dependencies readline-dev ncurses-dev &&
\  
cd /tmp && curl \--retry 5 \--max-time 120 \--connect-timeout 5 -fsSL \  
'http://downloads.sourceforge.net/project/java-readline/java-
readline/0.8.0/libreadline-
java-0.8.0-src.tar.gz?r=&ts=1463492548&use_mirror=freefr' | \  
tar xfz - && \  
cd /tmp/libreadline-java-* && \  
sed -r -i 's/install: jar build-native apidoc/install: jar build-native/'
Makefile && \  
sed -r -i 's|^.*cp -r api.*$||' Makefile && \  
sed -r -i 's/-ltermcap/-lncurses/g' src/native/Makefile && \  
make && make install && \  
rm -rf /tmp/libreadline* && \  
echo "*** libjava-readline INSTALLED *** " && \  
cd /tmp && curl \--retry 5 \--max-time 120 \--connect-timeout 5 -fsSL -o
henplus.zip https://github.com/bokysan/henplus/archive/master.zip && \  
unzip -q henplus.zip && rm henplus.zip && \  
cd henplus* && \  
ant jar && ant install && \  
echo "*** HENPLUS INSTALLED ***" && \  
mkdir -p /usr/share/henplus/ && cd /usr/share/henplus/ && \  
echo "*** Download postgresql driver..." && \  
curl \--retry 5 \--max-time 120 \--connect-timeout 5 -fsSL -O
https://jdbc.postgresql.org/download/postgresql-9.4.1208.jar && \  
(apk del build-base gcc g++ make eadline-dev ncurses-dev || true) && \  
(rm -rf /usr/lib/ant || true) && \  
(rm -rf /var/cache/apk/* > /dev/null || true) && (rm -rf /tmp/* > /dev/null ||
true) && \  
echo "*** Switching on UTF-8 handling..." && \  
sed -r -i 's/^JAVA_FLAGS=$/JAVA_FLAGS="-Dfile.encoding=UTF-8
-Djava.awt.headless=true"/' /usr/bin/henplus  
# Add other drivers  
COPY jdbc/ /usr/share/henplus/  
  
ENTRYPOINT [ "/usr/bin/henplus" ]  

