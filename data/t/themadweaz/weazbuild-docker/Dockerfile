FROM ubuntu:16.04  
# Install Necessary Tools  
RUN \  
apt-get update && \  
apt-get install -y apt-transport-https ca-certificates software-properties-
common sudo xdg-utils xvfb libxi6 libgconf-2-4 && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# Install docker-compose  
ENV DOCKER_COMPOSE_RELEASE_VERSION 1.15.0  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends curl && \  
curl -fsSL
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_RELEASE_VERSION}/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
apt-get remove -y curl && rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# Install OracleJDK  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update -qqy && \  
apt-get install -y oracle-java8-installer && \  
update-alternatives --config java && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# Install Chrome  
ARG CHROME_VERSION="google-chrome-stable"  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends curl && \  
curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
- && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update -qqy && \  
apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} && \  
apt-get remove -y curl && rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# Xvfb init.d  
COPY xvfb /etc/init.d/xvfb  
RUN chmod +x /etc/init.d/xvfb  
  
# Copy entry script, make executable  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Setup a non-privlaged user (as default) with password-less sudo  
RUN \  
useradd -ms /bin/bash cirunner -G sudo && \  
echo "cirunner ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/cirunner && \  
mkdir /builds && chown cirunner:cirunner /builds  
USER cirunner  
WORKDIR /home/cirunner  
  
# Set that java on the path  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
ENV PATH="${JAVA_HOME}/bin:${PATH}"  
  
  
ENTRYPOINT ["entrypoint.sh"]

