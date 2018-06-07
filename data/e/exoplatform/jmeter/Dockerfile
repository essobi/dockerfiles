# Dockerizing JMETER  
#  
# build : docker build -t exoplatform/jmeter .  
#  
FROM exoplatform/base-jdk:jdk8  
LABEL maintainer="eXo Platform <docker@exoplatform.com>"  
  
ARG JMETER_VERSION=3.3  
# Install GOSU  
RUN set -ex \  
&& ( \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
|| gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
|| gpg --keyserver keyserver.pgp.com --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
)  
  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Install JMETER  
RUN cd /usr/local && wget -O jmeter.tgz
https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz && tar xzf jmeter.tgz \  
&& ln -s apache-jmeter-${JMETER_VERSION} jmeter && rm jmeter.tgz  
  
RUN cd /usr/local/jmeter/lib/ext && wget -O plugins-manager.jar
https://jmeter-plugins.org/get/  
  
# Install Console status logger 0.1  
RUN cd /usr/local/jmeter && wget -O plugin.zip https://jmeter-
plugins.org/files/packages/jpgc-csl-0.1.zip && unzip plugin.zip && rm
plugin.zip  
  
# Install Custom Thread Group 2.4  
RUN cd /usr/local/jmeter && wget -O plugin.zip https://jmeter-
plugins.org/files/packages/jpgc-casutg-2.4.zip && unzip plugin.zip && rm
plugin.zip  
  
# Install entrypoint  
COPY entrypoint.sh /  
RUN chmod 755 /entrypoint.sh  
  
RUN mkdir -p /scripts && chmod 755 /scripts \  
&& mkdir -p /output && chmod 777 /output  
  
WORKDIR /output  
  
####  
## Configuration  
RUN echo "# This switch is needed for some JMeter Plugins reports" >>
/usr/local/jmeter/bin/user.properties \  
&& echo "jmeter.save.saveservice.thread_counts=true" >>
/usr/local/jmeter/bin/user.properties \  
&& echo "jmeter.save.saveservice.output_format=xml" >>
/usr/local/jmeter/bin/user.properties  
  
ENV JVM_ARGS="-Duser.language=en -Duser.region=EN"  
ENV JMETER_PROPERTY_PREFIX=JMETERPROP_  
  
ENTRYPOINT ["/entrypoint.sh"]  

