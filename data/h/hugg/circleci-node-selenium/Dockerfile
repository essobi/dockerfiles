FROM circleci/node:6.11.1-browsers  
  
# No interactive frontend during docker build  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
USER root  
RUN sed -i -e 's/deb\\.debian\\.org/http.debian.net/' /etc/apt/sources.list &&
\  
echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get -qqy update \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
tzdata \  
sudo \  
unzip \  
wget \  
&& apt-get -qqy -t jessie-backports install openjdk-8-jre-headless \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV TZ "UTC"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN echo 'circleci:secret' | chpasswd  
  
#===================================================  
# Run the following commands as non-privileged user  
#===================================================  
USER circleci  
  
#==========  
# Selenium  
#==========  
RUN sudo mkdir -p /opt/selenium \  
&& sudo chown circleci:circleci /opt/selenium \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/3.4/selenium-server-standalone-3.4.0.jar \  
-O /opt/selenium/selenium-server-standalone.jar  
  
#============================  
# Some configuration options  
#============================  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
#========================  
# Selenium Configuration  
#========================  
# As integer, maps to "maxInstances"  
ENV NODE_MAX_INSTANCES 1  
# As integer, maps to "maxSession"  
ENV NODE_MAX_SESSION 1  
# As integer, maps to "port"  
ENV NODE_PORT 5555  
# In milliseconds, maps to "registerCycle"  
ENV NODE_REGISTER_CYCLE 5000  
# In milliseconds, maps to "nodePolling"  
ENV NODE_POLLING 5000  
# In milliseconds, maps to "unregisterIfStillDownAfter"  
ENV NODE_UNREGISTER_IF_STILL_DOWN_AFTER 60000  
# As integer, maps to "downPollingLimit"  
ENV NODE_DOWN_POLLING_LIMIT 2  
# As string, maps to "applicationName"  
ENV NODE_APPLICATION_NAME ""  
# Following line fixes https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
#====================================  
# Scripts to run Selenium Standalone  
#====================================  
COPY entry_point.sh /opt/bin/entry_point.sh  
  
ENTRYPOINT /opt/bin/entry_point.sh  
  
EXPOSE 4444  

