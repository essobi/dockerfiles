FROM tomcat:8.0  
ENV TOMCAT_USER dspace  
ENV DS_VERSION 6.2  
ENV JAVA_OPTS "-XX:+UseParallelGC -Xmx4096m -Xms4096m -Dfile.encoding=UTF-8"  
RUN useradd -m dspace  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
RUN curl -SsL
https://github.com/DSpace/DSpace/archive/dspace-$DS_VERSION.tar.gz | tar -C
/usr/src/ -xzf -  
RUN mkdir /dspace && chown -R dspace /dspace /usr/src/DSpace-
dspace-$DS_VERSION  
  
ADD local.cfg.EXAMPLE /usr/src/DSpace-
dspace-$DS_VERSION/dspace/config/local.cfg  
RUN chmod 644 /usr/src/DSpace-dspace-$DS_VERSION/dspace/config/local.cfg &&
chown dspace:dspace /usr/src/DSpace-dspace-$DS_VERSION/dspace/config/local.cfg  
  
RUN buildDep=" \  
git \  
ant \  
openjdk-7-jdk \  
"; apt-get update && apt-get install -y $buildDep  
  
RUN cd /usr/src && curl
http://mirrors.fe.up.pt/pub/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar -C . -xzf -  
ENV PATH /usr/src/apache-maven-3.3.9/bin:${PATH}  
  
RUN cd /usr/src/DSpace-dspace-$DS_VERSION \  
&& sed -i "s/path=\"Mirage\/\"/path=\"Mirage2\/\"/" /usr/src/DSpace-
dspace-$DS_VERSION/dspace/config/xmlui.xconf \  
&& gosu dspace bash -c 'mvn package -Dmirage2.on=true' \  
&& sed -i "s/<java classname=\"org.dspace.app.launcher.ScriptLauncher\"
classpathref=\"class.path\" fork=\"yes\" failonerror=\"yes\">/<java
classname=\"org.dspace.app.launcher.ScriptLauncher\"
classpathref=\"class.path\" fork=\"yes\" failonerror=\"no\">/"
/usr/src/DSpace-dspace-$DS_VERSION/dspace/target/dspace-installer/build.xml  
  
ADD messages_pt_BR.xml /usr/src/DSpace-dspace-$DS_VERSION/dspace-
xmlui/src/main/webapp/i18n/messages_pt_BR.xml  
ADD pom.xml /usr/src/DSpace-
dspace-$DS_VERSION/dspace/modules/additions/pom.xml  
  
RUN cd /usr/src/DSpace-dspace-$DS_VERSION/dspace/target/dspace-installer \  
&& gosu dspace ant fresh_install \  
&& cd /dspace \  
&& rm -r /usr/src/* \  
&& apt-get purge -y --auto-remove $buildDep && rm -rf /var/lib/apt/lists/*
/tmp/*  
  
RUN cd /dspace/webapps/rest/WEB-INF \  
&& sed -i "s@<security-constraint>@<!--<security-constraint>@g" web.xml \  
&& sed -i "s@</security-constraint>@</security-constraint>\-->@g" web.xml  
  
RUN cd /dspace/config \  
&& sed -i 's@<!--<aspect name="Versioning Aspect"
path="resource://aspects/Versioning/" />\-->@<aspect name="Versioning Aspect"
path="resource://aspects/Versioning/" />@g' xmlui.xconf  
  
#CRON  
RUN apt-get update && apt-get install -y cron rsyslog  
ADD cronjobConfiguration /home/dspace/cronjobConfiguration  
RUN su - dspace && cd /home/dspace && crontab cronjobConfiguration  
#END - CRON  
COPY create-admin.sh /sbin/create-admin.sh  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["run"]  
  

