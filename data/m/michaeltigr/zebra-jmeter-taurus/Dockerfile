FROM ubuntu:16.04  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# Install base.  
RUN apt-get update \  
&& apt-get -y install \  
bash \  
build-essential \  
curl \  
openssl \  
procps \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Taurus.  
RUN apt-get update \  
&& apt-get -y install \  
libxslt1.1 \  
libxslt1-dev \  
libxml2 \  
libxml2-dev \  
python-pip \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install bzt==1.11.1  
  
# Install Java, jmeter.  
ENV JAVA_HOME /usr  
RUN apt-get update \  
&& apt-get -y install openjdk-8-jre-headless maven \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install jMeter.  
ENV JMETER_VERSION 4.0  
ENV JMETER_HOME=/apache-jmeter  
RUN curl -o /apache-jmeter.tgz
https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz \  
&& tar -C / -xzf /apache-jmeter.tgz \  
&& rm /apache-jmeter.tgz \  
&& mv /apache-jmeter-${JMETER_VERSION} ${JMETER_HOME} \  
&& rm ${JMETER_HOME}/bin/user.properties  
  
COPY user.properties ${JMETER_HOME}/bin/  
  
# Install plugins.  
RUN curl -L -o ${JMETER_HOME}/lib/ext/jmeter-plugins-manager.jar -O
https://jmeter-plugins.org/get/ \  
&& curl -L -o ${JMETER_HOME}/lib/cmdrunner-2.2.jar
http://search.maven.org/remotecontent?filepath=kg/apc/cmdrunner/2.2/cmdrunner-2.2.jar
\  
&& java -cp ${JMETER_HOME}/lib/ext/jmeter-plugins-manager.jar
org.jmeterplugins.repository.PluginManagerCMDInstaller \  
&& ${JMETER_HOME}/bin/PluginsManagerCMD.sh available \  
&& ${JMETER_HOME}/bin/PluginsManagerCMD.sh install-all-except  
  
ENTRYPOINT ["bzt"]  
  

