FROM ubuntu:14.04  
MAINTAINER Intelag SpA, sergio@intelag.net  
  
RUN mkdir /home/meteorapp  
  
WORKDIR /home/meteorapp  
  
ADD . ./meteorapp  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Do basic updates  
RUN apt-get update -q && apt-get clean  
  
# Get curl in order to download curl  
RUN apt-get install curl -y \  
  
# Install Meteor  
&& (curl https://install.meteor.com/?release=1.4.1.3 | sh) \  
  
# Build the Meteor app  
&& cd /home/meteorapp/meteorapp/app \  
  
&& meteor build ../build --directory --allow-superuser \  
  
# Install the version of Node.js we need.  
&& cd /home/meteorapp/meteorapp/build/bundle \  
&& bash -c 'curl
"https://nodejs.org/dist/$(<.node_version.txt)/node-$(<.node_version.txt)-linux-x64.tar.gz"
> /home/meteorapp/meteorapp/build/required-node-linux-x64.tar.gz' \  
&& cd /usr/local && tar --strip-components 1 -xzf
/home/meteorapp/meteorapp/build/required-node-linux-x64.tar.gz \  
&& rm /home/meteorapp/meteorapp/build/required-node-linux-x64.tar.gz \  
  
# Build the NPM packages needed for build  
&& cd /home/meteorapp/meteorapp/build/bundle/programs/server \  
&& npm install --no-bin-links \  
  
  
# Get rid of Meteor. We're done with it.  
&& rm /usr/local/bin/meteor \  
&& rm -rf ~/.meteor \  
  
#no longer need curl  
&& apt-get --purge autoremove curl -y  
RUN npm install -g forever  
  
EXPOSE 80  
ENV PORT 80  
ENV METEOR_NO_RELEASE_CHECK true  
CMD ["forever", "--minUptime", "1000", "--spinSleepTime", "1000",
"meteorapp/build/bundle/main.js"]  

