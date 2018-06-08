FROM node:7.10.0  
MAINTAINER Intelag SpA, sergio@intelag.net  
  
RUN mkdir /home/meteorapp  
  
WORKDIR /home/meteorapp  
  
ADD . ./meteorapp  
  
# Install Meteor  
RUN (curl https://install.meteor.com/ | sh) \  
&& cd /home/meteorapp/meteorapp/app \  
&& meteor npm install \  
&& meteor build ../build --directory --allow-superuser \  
&& cd /home/meteorapp/meteorapp/build/bundle/programs/server \  
&& npm install --production --no-bin-links \  
&& npm install -g forever \  
&& npm uninstall fibers \  
&& npm install fibers \  
# Get rid of Meteor. We're done with it.  
&& rm /usr/local/bin/meteor \  
&& rm -rf ~/.meteor  
  
  
  
  
EXPOSE 80  
ENV PORT 80  
ENV METEOR_NO_RELEASE_CHECK true  
CMD ["forever", "--minUptime", "1000", "--spinSleepTime", "1000",
"meteorapp/build/bundle/main.js"]  

