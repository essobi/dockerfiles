FROM java:9  
  
USER root  
ENV JMETER_VERSION 4.0  
ENV JMETER_HOME=/apache-jmeter  
ENV TAURUS_VERSION=1.11.0  
# Install dev depenedancies & Taurus (bzt)  
RUN apt-get update && \  
apt-get install -y \  
python \  
default-jre-headless \  
python-tk \  
python-pip \  
python-dev \  
libxml2-dev \  
libxslt-dev \  
zlib1g-dev \  
net-tools \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Install Taurus (bzt)  
RUN pip install bzt==${TAURUS_VERSION}  
  
# Install Jmeter  
RUN curl -o /apache-jmeter.tgz
http://apache.mirror.serversaustralia.com.au//jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz \  
&& tar -C / -xzf /apache-jmeter.tgz \  
&& rm /apache-jmeter.tgz \  
&& mv /apache-jmeter-${JMETER_VERSION} ${JMETER_HOME} \  
&& rm ${JMETER_HOME}/bin/user.properties  
  
# Install Jmeter Plugins  
RUN curl -L -o ${JMETER_HOME}/lib/ext/jmeter-plugins-manager.jar -O
https://jmeter-plugins.org/get/ && \  
curl -L -o ${JMETER_HOME}/lib/cmdrunner-2.0.jar
http://search.maven.org/remotecontent?filepath=kg/apc/cmdrunner/2.0/cmdrunner-2.0.jar
&& \  
java -cp ${JMETER_HOME}/lib/ext/jmeter-plugins-manager.jar
org.jmeterplugins.repository.PluginManagerCMDInstaller && \  
ln -s /usr/lib/jvm/java-9-openjdk-amd64/lib /usr/lib/jvm/java-9-openjdk-
amd64/conf && \  
${JMETER_HOME}/bin/PluginsManagerCMD.sh available && \  
${JMETER_HOME}/bin/PluginsManagerCMD.sh install-all-except && \  
${JMETER_HOME}/bin/PluginsManagerCMD.sh status && \  
ls -ltr ${JMETER_HOME}/lib/ext/

