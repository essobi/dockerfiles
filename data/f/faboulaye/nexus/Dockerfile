FROM faboulaye/openjdk  
MAINTAINER Firdaws Aboulaye "aboufred@gmail.com"  
ENV NEXUS_VERSION=3.9.0-01 \  
NEXUS_HOME=/opt/sonatype/nexus \  
NEXUS_DATA=/nexus-data \  
PATH=$NEXUS_HOME/bin:$PATH \  
JAVA_MIN_MEM="1200M" \  
JAVA_MAX_MEM="1200M"  
RUN mkdir -p $NEXUS_HOME $NEXUS_DATA \  
&& apt-get update \  
&& apt-get install -y wget vim\  
&& wget --no-check-certificate --no-cookies
https://download.sonatype.com/nexus/3/nexus-$NEXUS_VERSION-unix.tar.gz \  
&& wget --no-check-certificate --no-cookies
http://download.sonatype.com/nexus/3/nexus-$NEXUS_VERSION-unix.tar.gz.md5 \  
&& echo "$(cat nexus-$NEXUS_VERSION-unix.tar.gz.md5) nexus-$NEXUS_VERSION-
unix.tar.gz" | md5sum -c \  
&& tar -zvxf nexus-$NEXUS_VERSION-unix.tar.gz --strip-components=1 -C
$NEXUS_HOME \  
&& groupadd --gid 1000 -r nexus \  
&& useradd -r --uid 1000 -c "nexus role account" -d $NEXUS_DATA -g nexus -s
/bin/false nexus \  
&& chown -R nexus:nexus $NEXUS_HOME $NEXUS_DATA\  
&& sed -e "s|-Xms1200M|-Xms${JAVA_MIN_MEM}|g" \  
-e "s|-Xmx1200M|-Xmx${JAVA_MAX_MEM}|g" \  
-e "s|karaf.home=.|karaf.home=$NEXUS_HOME|g" \  
-e "s|karaf.base=.|karaf.base=$NEXUS_HOME|g" \  
-e "s|karaf.etc=etc/karaf|karaf.etc=$NEXUS_HOME/etc|g" \  
-e "s|karaf.data=../sonatype-work/nexus3|karaf.data=$NEXUS_DATA|g" \  
-e "s|LogFile=../sonatype-work/nexus3/log/jvm.log|LogFile=$NEXUS_DATA/log/jvm.log|g" \  
-e "s|java.io.tmpdir=../sonatype-work/nexus3/tmp|java.io.tmpdir=$NEXUS_DATA/tmp|g" \  
-i $NEXUS_HOME/bin/nexus.vmoptions \  
&& apt-get remove -y wget \  
&& rm -rf nexus-$NEXUS_VERSION-unix.tar.gz nexus-$NEXUS_VERSION-
unix.tar.gz.md5 \  
/tmp/* /var/log/* /var/cache/* /usr/share/man/?? /usr/share/man/??_*
/var/lib/apt/lists/*  
  
USER nexus  
VOLUME $NEXUS_DATA  
EXPOSE 8081 18080 18443  
WORKDIR $NEXUS_HOME  
CMD ["bin/nexus", "run"]  

