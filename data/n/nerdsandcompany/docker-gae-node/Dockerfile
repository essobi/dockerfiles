# Dockerfile extending the generic Node image with application files for a  
# single application.  
FROM gcr.io/google_appengine/nodejs  
MAINTAINER Bob Olde Hampsink <b.oldehampsink@nerds.company>  
  
WORKDIR /app  
  
# Install packages  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" |
tee /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee
/etc/apt/sources.list.d/google-chrome.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& apt-get update -qqy && apt-get install -qqy google-cloud-sdk google-chrome-
stable openssh-client \  
&& rm /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copy ssh config to image  
COPY .ssh/ /root/.ssh/  
RUN chmod 0600 /root/.ssh/id_rsa  
  
# Following line fixes  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
# Use devDependencies as well  
ENV NODE_ENV development  
  
# Locate our binaries  
ENV PATH /app/node_modules/.bin:$PATH  
  
# You have to specify "--unsafe-perm" with npm install  
# when running as root. Failing to do this can cause  
# install to appear to succeed even if a preinstall  
# script fails, and may have other adverse consequences  
# as well.  
# This command will also cat the npm-debug.log file after the  
# build, if it exists.  
ONBUILD ADD package*.json /app/  
ONBUILD RUN npm install --unsafe-perm || \  
((if [ -f npm-debug.log ]; then \  
cat npm-debug.log; \  
fi) && false)  
  
# Copy files to app  
ONBUILD ADD . /app/  

