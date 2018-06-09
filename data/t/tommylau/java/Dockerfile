FROM ubuntu:16.04  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# Non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Export Java Home  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Install Oracle JDK 1.8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update -qq \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& apt-get install -y --no-install-recommends ca-certificates curl
libtcnative-1 oracle-java8-installer \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
&& ln -s /usr/lib/x86_64-linux-gnu/libtcnative-1.so /usr/lib/libtcnative-1.so
\  
&& sed -i 's/^\\(securerandom.source=file:\/dev\/\\)\\(random\\)/\1u\2/'
${JAVA_HOME}/jre/lib/security/java.security  
# Due to import control restrictions of some countries, the version of the JCE
policy files that are bundled in the Java Runtime Environment, or JRE(TM), 8
environment allow "strong" but limited cryptography to be used. This download
bundle (the one including this README file) provides "unlimited strength"
policy files which contain no restrictions on cryptographic strengths.  
# Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy
Files 8 Download  
#
http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html  
# http://stackoverflow.com/questions/30758303/problems-connecting-via-https-
ssl-through-own-java-client  
COPY local_policy.jar ${JAVA_HOME}/jre/lib/security/  

