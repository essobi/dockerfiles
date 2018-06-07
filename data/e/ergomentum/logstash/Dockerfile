FROM centos:7.4.1708 as builder  
ENV LANG='C' LANGUAGE='C' LC_ALL='C'  
RUN mkdir -p /target  
RUN yum --installroot=/target --releasever=/ install -y bash  
RUN rm -rf /target/usr/share/{man,doc,info,gnome/help} /target/var/cache/yum  
RUN localedef --prefix=/target --list-archive|xargs localedef --prefix=/target
--delete-from-archive  
RUN mv /target/usr/lib/locale/locale-archive{,.tmpl}  
RUN chroot /target build-locale-archive  
RUN \  
mkdir -p /target/usr/java && curl -jksSLH "Cookie: oraclelicense=accept-
securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/server-
jre-8u162-linux-x64.tar.gz | \  
tar \  
xz \  
-C /target/usr/java \  
\--strip-components=1 \  
\--exclude='man' \  
\--exclude='release'  
  
FROM centos:7.4.1708 as logstash  
RUN \  
mkdir -p /target && \  
curl -Lo -
https://artifacts.elastic.co/downloads/logstash/logstash-6.2.3.tar.gz | \  
tar \  
xz \  
-C /target \  
\--strip-components=1 \  
\--exclude='config/jvm.options' \  
\--exclude='bin'  
COPY config /target/config  
COPY pipeline /target/pipeline  
  
FROM scratch  
ENV \  
LANG='C' \  
LANGUAGE='C' \  
LC_ALL='C' \  
LOGSTASH_HOME="/usr/share/logstash" \  
LS_HOME="/usr/share/logstash" \  
JAVACMD='/usr/java/bin/java' \  
JAVA_OPTS="\  
-Xms1g \  
-Xmx1g \  
-XX:+UseParNewGC \  
-XX:+UseConcMarkSweepGC \  
-XX:CMSInitiatingOccupancyFraction=75 \  
-XX:+UseCMSInitiatingOccupancyOnly \  
-Djava.awt.headless=true \  
-Dfile.encoding=UTF-8 \  
-Djruby.compile.invokedynamic=true \  
-Djruby.jit.threshold=0 \  
-XX:+HeapDumpOnOutOfMemoryError \  
-Djava.security.egd=file:/dev/urandom\  
" \  
GEM_HOME="/usr/share/logstash/vendor/bundle/jruby/2.3.0" \  
GEM_PATH="/usr/share/logstash/vendor/bundle/jruby/2.3.0"  
COPY \--from=builder /target .  
  
#COPY --from=logstash --chown=1000:1000 /target /usr/share/logstash  
# Workaround for https://forums.docker.com/t/copy-chown-fails-in-automated-
build-unknown-flag-chown/43059/5  
COPY \--from=builder /usr/bin/chown /usr/bin/rm /usr/bin/  
COPY \--from=logstash /target /usr/share/logstash  
RUN chown 1000:1000 -R /usr/share/logstash && rm /usr/bin/{chown,rm}  
  
WORKDIR /usr/share/logstash  
VOLUME /usr/share/logstash/config  
VOLUME /usr/share/logstash/data  
VOLUME /usr/share/logstash/pipeline  
USER 1000  
EXPOSE 9600 12201/udp  
ENTRYPOINT [\  
"/usr/java/bin/java",\  
"-Xms256m",\  
"-Xmx256m",\  
"-XX:+UseParNewGC",\  
"-XX:+UseConcMarkSweepGC",\  
"-XX:CMSInitiatingOccupancyFraction=75",\  
"-XX:+UseCMSInitiatingOccupancyOnly",\  
"-Djava.awt.headless=true",\  
"-Dfile.encoding=UTF-8",\  
"-Djruby.compile.invokedynamic=true",\  
"-Djruby.jit.threshold=0",\  
"-XX:+HeapDumpOnOutOfMemoryError",\  
"-Djava.security.egd=file:/dev/urandom",\  
"-cp",\  
"/usr/share/logstash/logstash-core/lib/jars/*",\  
"org.logstash.Logstash"\  
]  

