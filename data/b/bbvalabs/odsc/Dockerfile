FROM python:3.5-slim  
  
ENV GOSU_VERSION=1.9 \  
PYTHONPATH="/odsc"  
# Update OS, add new user  
RUN useradd -ms /bin/bash web  
  
# Install Gosu to run with unprivileged user  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget curl unzip
git p7zip \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Configure GIT  
RUN git config --global http.sslVerify false  
  
#  
# Install Languajes VM  
#  
# Python requirements  
RUN apt-get install -y --no-install-recommends gcc python3-dev libpq-dev  
  
# NodeJs  
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
apt-get -y --no-install-recommends install nodejs build-essential libssl-dev  
  
# Java 8  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update  
  
RUN apt install -y -t jessie-backports openjdk-8-jre-headless ca-certificates-
java  
  
#  
# Install Analysis tools  
#  
# Install OWASP Dependency Check  
RUN wget -O /tmp/current.txt
http://jeremylong.github.io/DependencyCheck/current.txt && \  
current=$(cat /tmp/current.txt) && wget https://dl.bintray.com/jeremy-
long/owasp/dependency-check-$current-release.zip && \  
unzip dependency-check-$current-release.zip && mv dependency-check /usr/share/
&& \  
chown -R web:web /usr/share/dependency-check && \  
ln -s /usr/share/dependency-check/bin/dependency-check.sh /usr/bin/dependency-
check  
  
# Copy database snapshot  
COPY ./odsc/security_dependency_check/plugins/dc.h2.db.7z /tmp/  
  
# Uncompress the snapshot  
RUN mkdir /usr/share/dependency-check/data && \  
cd /usr/share/dependency-check/data && \  
p7zip -d /tmp/dc.h2.db.7z  
  
# Install Retire.js  
RUN npm -g install retire  
  
#  
# Install the project code  
#  
# Create folders and get the code  
RUN mkdir /odsc /logs  
  
# Build dependencies  
COPY ./odsc/requirements.txt /odsc/  
RUN cd /odsc && pip install --upgrade pip && pip install -r
/odsc/requirements.txt  
  
# Copy site code  
COPY ./odsc /odsc/  
  
# Copy NGINX config  
COPY ./nginx_config.conf /odsc/default.conf  
  
# Enable scripts  
RUN chown -R web:web /odsc /logs && \  
chmod 755 /odsc /logs && \  
chmod +x /odsc/*.sh  
  
WORKDIR /odsc  
  
# Clean APT cache  
RUN apt-get clean

