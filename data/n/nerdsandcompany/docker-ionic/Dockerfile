# Inherit from Heroku's stack  
FROM heroku/heroku:16  
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
  
# Install Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install xvfb google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dependencies  
ONBUILD ADD ["package.json", "package-lock.json", "/app/user/"]  
ONBUILD RUN /app/heroku/node/bin/npm install  
  
# Add files  
ONBUILD ADD . /app/user/  

