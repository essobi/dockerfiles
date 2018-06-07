#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
  
FROM buildpack-deps:buster-scm  
  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
dirmngr \  
gnupg \  
unzip \  
&& (echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu devel main" >
/etc/apt/sources.list.d/webupd8team-ubuntu-java.list) \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \  
&& (echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections) \  
&& (echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections) \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
oracle-java8-installer \  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*_dists_*  
  
# If you're reading this and have any feedback on how this image could be  
# improved, please open an issue or a pull request so we can discuss it!  

