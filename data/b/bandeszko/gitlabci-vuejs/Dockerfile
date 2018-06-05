FROM gitlab/gitlab-runner:latest  
  
MAINTAINER tandris  
  
ENV GITLAB_CI_URL=yourgitlabci.com  
ENV GITLAB_CI_TOKEN=runners  
ENV GITLAB_CI_NAME=vuejs  
ENV GITLAB_CI_EXECUTOR=shell  
ENV LC_ALL=en_US.UTF-8  
ENV DISPLAY=:99  
ENV SONAR_HOST_URL=myserver:9000  
ENV SONAR_JDBC_URL=jdbc:postgresql:\/\/localhost\/sonar  
ENV SONAR_JDBC_USER=sonar  
ENV SONAR_JDBC_PWD=sonar  
ENV MAVEN_SETTINGS=/home/gitlab-runner/.m2/settings.xml  
  
RUN apt-get update  
RUN sudo locale-gen en_US.UTF-8  
RUN sudo dpkg-reconfigure locales  
  
# Install Java, maven, sonar.  
RUN \  
apt-get install -q -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -q -y oracle-java8-installer && \  
apt-get install -q -y wget unzip  
  
RUN \  
wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/2.4/sonar-runner-dist-2.4.zip && \  
unzip sonar-runner-dist-2.4.zip && \  
mv sonar-runner-2.4 /opt/sonar-runner  
  
COPY settings.xml /home/gitlab-runner/.m2/settings.xml  
  
# Install maven and git.  
RUN apt-get install -q -y maven git  
RUN apt-get clean  
  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.10.1  
RUN apt-get update  
RUN apt-get install -y xz-utils mc  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Chrome install to run phantomjs tests  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
# Firefox install  
RUN \  
wget
https://sourceforge.net/projects/ubuntuzilla/files/mozilla/apt/pool/main/f/firefox-
mozilla-build/firefox-mozilla-build_52.0.1-0ubuntu1_amd64.deb && \  
dpkg -i firefox-mozilla-build_52.0.1-0ubuntu1_amd64.deb  
  
RUN apt-get update -y  
RUN apt-get install -y -q \  
xvfb  
  
EXPOSE 4444 5999  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

