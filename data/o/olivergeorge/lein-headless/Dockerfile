FROM clojure:lein-2.6.1  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update  
RUN apt-get -y install google-chrome-beta nodejs npm nodejs-legacy sudo
libnss3  
  
# Borrowed from  
# https://github.com/yukinying/chrome-headless-browser-
docker/blob/master/chrome/Dockerfile#L22  
RUN useradd headless --shell /bin/bash --create-home \  
&& usermod -a -G sudo headless \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'headless:nopassword' | chpasswd  
  
RUN mkdir /data && chown -R headless:headless /data  
  
# Borrowed from PhantomJS Docker file and trimmed  
# Ref https://hub.docker.com/r/wernight/phantomjs/~/dockerfile/  
RUN apt-get install -y --no-install-recommends \  
ca-certificates \  
bzip2 \  
libfontconfig  
  
RUN set -x \  
# Install official PhantomJS release  
&& apt-get update \  
&& apt-get install -y --no-install-recommends curl \  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin  
  
RUN npm install karma karma-cljs-test --save-dev \  
&& npm install -g karma-cli \  
&& npm install karma-chrome-launcher karma-firefox-launcher --save-dev  

