FROM openjdk:latest  
  
RUN apt-get update && apt-get install -y build-essential apt-transport-https
ca-certificates curl gnupg2 software-properties-common tar  
  
## Install Node  
RUN curl -sL https://deb.nodesource.com/setup_9.x > install.sh && chmod +x
install.sh && ./install.sh  
RUN apt-get install -y nodejs  
  
## Docker Compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
## Docker  
RUN curl
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz >
docker.tar.gz && tar xzvf docker.tar.gz -C /usr/local/bin/ --strip-
components=1  
RUN rm docker.tar.gz && docker -v  
  
## PhantomJS  
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list.d/phantomjs.list  
RUN apt-get update && apt-get install -y phantomjs  
  
## Rancher Compose  
RUN curl -L https://github.com/rancher/rancher-
compose/releases/download/v0.12.5/rancher-compose-linux-amd64-v0.12.5.tar.xz |
tar xJvf - --strip-components=2 -C /usr/local/bin/ && chmod +x
/usr/local/bin/rancher-compose  
  
## Gradle  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.5.1  
RUN wget --output-document=gradle.zip
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN unzip gradle.zip \  
&& rm gradle.zip \  
&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \  
&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle  
  
# Neustes npm  
RUN npm install -g npm@latest  
  
## emundo User  
RUN addgroup --gid 1101 rancher && \  
# Für RancherOS brauchen wir diese Gruppe:
http://rancher.com/docs/os/v1.1/en/system-services/custom-system-
services/#creating-your-own-console  
addgroup --gid 999 aws && \  
# Für die AWS brauchen wir diese Gruppe  
useradd -ms /bin/bash emundo && \  
adduser emundo sudo && \  
# Das ist notwendig, damit das Image in RancherOS funktioniert  
usermod -aG 999 emundo && \  
# Das ist notwendig, damit das Image in RancherOS funktioniert  
usermod -aG 1101 emundo && \  
# Das ist notwendig, damit das Image lokal funktioniert  
usermod -aG root emundo  
  
USER emundo  
WORKDIR /home/emundo  

