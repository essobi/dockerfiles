FROM java:8  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JMETER_VERSION 3.1  
ENV JMETER_PLUGINS_VERSION 1.4.0  
ENV JMETER_HOME /opt/jmeter  
ENV JMETER_DOWNLOAD_URL
http://mirror.serversupportforum.de/apache/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz  
  
# install needed debian packages & clean up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl tar ca-certificates unzip ant
&& \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# download and extract jmeter  
RUN mkdir -p ${JMETER_HOME} && \  
curl -L --silent ${JMETER_DOWNLOAD_URL} | tar -xz --strip=1 -C ${JMETER_HOME}  
RUN ln -s ${JMETER_HOME}/bin/jmeter /usr/local/bin/jmeter  
  
# install plugin  
RUN wget --directory-prefix=${JMETER_HOME}/lib
https://repo1.maven.org/maven2/kg/apc/cmdrunner/2.0/cmdrunner-2.0.jar  
RUN wget --directory-prefix=${JMETER_HOME}/lib/ext
https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/0.12/jmeter-
plugins-manager-0.12.jar  
RUN java -cp ${JMETER_HOME}/lib/ext/jmeter-plugins-manager-0.12.jar
org.jmeterplugins.repository.PluginManagerCMDInstaller  
  
RUN wget --directory-prefix=${JMETER_HOME}/lib/ext
http://search.maven.org/remotecontent?filepath=kg/apc/jmeter-plugins-
json/2.6/jmeter-plugins-json-2.6.jar  
RUN wget --directory-prefix=${JMETER_HOME}/lib/ext
https://search.maven.org/remotecontent?filepath=kg/apc/jmeter-plugins-
prmctl/0.3/jmeter-plugins-prmctl-0.3.jar  
#RUN ./${JMETER_HOME}/bin/PluginsManagerCMD.sh install jpgc-prmctl,jpgc-json  
RUN ./${JMETER_HOME}/bin/PluginsManagerCMD.sh status  
  
# Set ant build.xml  
ADD build.xml /tmp  
RUN mkdir /html && mv /tmp/build.xml /html/build.xml  
  
# Set jmeter property  
RUN echo log_file= >> ${JMETER_HOME}/bin/jmeter.properties  
  
# Add junit report support  
RUN mkdir /junit  
ADD junit/build.xml /junit  
ADD junit/jmeter-results-to-junit.xsl /junit  
  
WORKDIR ${JMETER_HOME}  
  

