FROM node:8.5.0  
LABEL author="Hiep Le, hieptuanle@gmail.com"  
  
WORKDIR /home/mean  
  
# Install Mean.JS Prerequisites  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  
RUN apt-get update \  
&& apt-get install libvips libvips-dev build-essential \  
libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 -y  
  
RUN apt-get install --fix-missing -y xvfb  
  
# Install Mean.JS packages  
ADD package.json /home/mean/package.json  
RUN npm install  
  
# Manually trigger bower. Why doesnt this work via npm install?  
ADD .bowerrc /home/mean/.bowerrc  
ADD bower.json /home/mean/bower.json  
RUN bower install --config.interactive=false \--allow-root  
  
# Make everything available for start  
ADD . /home/mean  
  
# currently only works for development  
ENV NODE_ENV cypress  
ENV MONGODB_URI mongo  
ENV REDIS_URI redis  
ENV HND_DOCKER 1  
# Port 3000 for server  
# Port 35729 for livereload  
EXPOSE 3000 35729  
CMD ["grunt", "cypress"]  

