# Inherit from Heroku's stack  
FROM heroku/heroku:16  
MAINTAINER Bob Olde Hampsink <b.oldehampsink@nerds.company>  
  
# Internally, we arbitrarily use port 3000  
ENV PORT 3000  
# Which version of node?  
ENV NODE_ENGINE 8.11.2  
# Locate our binaries  
ENV PATH /app/heroku/node/bin/:/app/user/node_modules/.bin:$PATH  
  
# Following line fixes  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
# Create some needed directories  
RUN mkdir -p /app/heroku/node /app/.profile.d  
WORKDIR /app/user  
  
# Install node  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node  
  
# Export the node path in .profile.d  
RUN echo "export
PATH=\"/app/heroku/node/bin:/app/user/node_modules/.bin:\$PATH\"" >
/app/.profile.d/nodejs.sh  
  
# Install protractor and webdriver globally  
RUN /app/heroku/node/bin/npm install -g protractor && webdriver-manager update
--standalone false \--gecko false  
  
# Add source for yarn  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install chrome (and yarn)  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install yarn xvfb google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  
# run npm or yarn install  
# add yarn.lock to .slugignore in your project  
ONBUILD ADD package*.json yarn.* /app/user/  
ONBUILD RUN [ -f yarn.lock ] && yarn install --no-progress || npm install  
  
# Add files  
ONBUILD ADD . /app/user/  

