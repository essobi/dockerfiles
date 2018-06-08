FROM debian:9  
RUN apt-get update && \  
apt-get install -y gnupg2 unzip  
  
RUN echo oracle-java10-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic main" |
tee /etc/apt/sources.list.d/linuxuprising-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 73C3DB2A &&
\  
apt-get update && \  
apt-get install -y oracle-java10-installer  
  
CMD ["gradle"]  
  
# Code below taken from: https://github.com/keeganwitt/docker-
gradle/blob/64a348e79cbe0bc8acb9da9062f75aca02bf3023/jdk10/Dockerfile  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.8  
ARG
GRADLE_DOWNLOAD_SHA256=fca5087dc8b50c64655c000989635664a73b11b9bd3703c7d6cabd31b7dcdb04  
RUN set -o errexit -o nounset \  
&& echo "Downloading Gradle" \  
&& wget --no-verbose --output-document=gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \  
\  
&& echo "Checking download hash" \  
&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum --check - \  
\  
&& echo "Installing Gradle" \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \  
&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \  
\  
&& echo "Adding gradle user and group" \  
&& groupadd --system --gid 1000 gradle \  
&& useradd --system --gid gradle --uid 1000 --shell /bin/bash --create-home
gradle \  
&& mkdir /home/gradle/.gradle \  
&& chown --recursive gradle:gradle /home/gradle \  
\  
&& echo "Symlinking root Gradle cache to gradle Gradle cache" \  
&& ln -s /home/gradle/.gradle /root/.gradle  
  
# Create Gradle volume  
USER gradle  
VOLUME "/home/gradle/.gradle"  
WORKDIR /home/gradle  
  
RUN set -o errexit -o nounset \  
&& echo "Testing Gradle installation" \  
&& gradle --version  

