FROM buildpack-deps:jessie-scm  
  
# Install node 6.x  
RUN set -x \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y \  
nodejs \  
&& npm install -g npm@3.8.9 # Due to https://github.com/npm/npm/issues/12647
for 3.9.0  
  
# Install Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >
/etc/apt/sources.list.d/google.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
xvfb \  
google-chrome-stable  
  
ADD dockerscripts/xvfb-chrome /usr/bin/xvfb-chrome  
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome  
RUN chmod 755 /usr/bin/google-chrome  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# Install firefox  
# RUN set -x \  
# && apt-get update \  
# && apt-get install -y \  
# pkg-mozilla-archive-keyring  
# RUN echo 'deb http://mozilla.debian.net/ jessie-backports firefox-release'
>> /etc/apt/sources.list.d/jessie-backports.list  
# RUN set -x \  
# && apt-get update \  
# && apt-get install -y \  
# xvfb \  
# && apt-get install -y -t \  
# jessie-backports \  
# firefox  
# ADD dockerscripts/xvfb-firefox /usr/bin/xvfb-firefox  
# RUN ln -sf /usr/bin/xvfb-firefox /usr/bin/firefox  
# ENV FIREFOX_BIN /usr/bin/firefox  
# This is needed for PhantomJS  
RUN set -x && \  
apt-get update && \  
apt-get install -y \  
bzip2  
  
# RUN node -v  
RUN npm -v  
# install angular/cli as global  
RUN npm install -g @angular/cli  
# RUN java -version  
# RUN mvn -v  
# RUN apt-cache policy firefox-esr | grep Installed | sed -e
"s/Installed/Firefox/"  
# RUN apt-cache policy chromium | grep Installed | sed -e
"s/Installed/Chrome/"  

