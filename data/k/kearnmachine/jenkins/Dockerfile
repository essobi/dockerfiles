FROM jenkins/jenkins:latest  
ARG user=jenkins  
  
USER root  
  
#launch4j 32bit libs (fix for windres: No such file or directory)  
#nodejs  
#chromium  
RUN apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_10.x | bash - \  
&& apt-get install -y lib32z1 lib32ncurses5 chromium ca-certificates nodejs \  
#cleanup  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "installed nodejs version: `nodejs --version`"  
  
#YARN (from _/node dockerfile)  
ENV YARN_VERSION 1.6.0  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
#restore previous used user for jenkins image  
USER ${user}

