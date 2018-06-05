FROM gitlab/gitlab-runner:latest  
  
MAINTAINER Gabor Rendes <rendesg@gmail.com>  
  
ENV GITLAB_CI_URL=yourgitlabci.com  
ENV GITLAB_CI_TOKEN=runners  
ENV GITLAB_CI_NAME=nodejs-meteor  
ENV GITLAB_CI_EXECUTOR=shell  
ENV LC_ALL=en_US.UTF-8  
ENV DISPLAY=:99  
RUN apt-get update  
RUN sudo locale-gen en_US.UTF-8  
RUN sudo dpkg-reconfigure locales  
  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.7.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
RUN curl https://install.meteor.com | sh  
RUN meteor update --release METEOR@1.3  
RUN npm i --unsafe-perm  
RUN npm i -g gulp tslint bower grunt-cli yo handlebars cucumber typings
typescript@1.8.0 dts-generator --unsafe-perm  
  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y xvfb  
  
COPY xvfb /etc/init.d/  
RUN chmod +x /etc/init.d/xvfb  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

