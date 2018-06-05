# Start with official node image.  
FROM node:6.1.0  
MAINTAINER astronomer <greg@astronomer.io>  
  
RUN apt-get update && \  
apt-get install -y expect wget ppp && \  
rm -rf /var/lib/apt/lists/*  
  
# Install fortivpn client unofficial .deb  
RUN wget 'https://hadler.me/files/forticlient-sslvpn_4.4.2329-1_amd64.deb' -O
forticlient-sslvpn_amd64.deb  
RUN dpkg -x forticlient-sslvpn_amd64.deb /usr/share/forticlient  
  
# Run setup  
RUN /usr/share/forticlient/opt/forticlient-sslvpn/64bit/helper/setup.linux.sh
2  
  
ADD forticlient /usr/local/bin/  
  
# Make directory for bunyan logs  
ONBUILD RUN mkdir -p /usr/local/src/log  
ONBUILD ENV LOG_PATH /usr/local/src/log  
  
ONBUILD WORKDIR /usr/local/src  
  
# copy package.json and install modules  
ONBUILD COPY package.json .  
ONBUILD RUN ["npm", "install"]  
  
# Add standard files on downstream builds.  
# Add lib and test last to use docker layer caching for previous layers  
# especially npm install. Avoids downstream images needing to run npm install  
# on every change to lib or test files  
ONBUILD COPY .babelrc .  
ONBUILD COPY .eslintrc .  
ONBUILD COPY lib lib  
ONBUILD COPY test test  
  
# Execute task-runner installed with the activity with arguments provided from
CMD.  
# We might want to split out the executor and the utils into aries-executor
and aries-utils.  
ENTRYPOINT ["node_modules/.bin/aries-data"]  

