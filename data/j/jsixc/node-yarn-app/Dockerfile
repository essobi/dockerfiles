FROM node:7  
# Remove the outdated version of yarn that is installed by the node image  
RUN rm -f /usr/local/bin/yarn  
  
# Install yarn package manager  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3 \  
&& apt-get update -qq && apt-get install -y -qq yarn \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/  
  
# Install node-gyp  
RUN npm install -g node-gyp  
  
# Create a user called `app`  
RUN useradd -ms /bin/bash app  
# Switch to running as the user called app  
WORKDIR /home/app  
  
# Copy across package.json and yarn.lock and  
# install depedencies.  
# This is a separate step so it can be cached and the  
# cache is used when not changing depedencies  
ONBUILD COPY package.json yarn.lock /home/app/  
ONBUILD RUN yarn install --pure-lockfile  
  
ONBUILD COPY . /home/app  
ONBUILD RUN chown -R app:app /home/app  
ONBUILD USER app  
  
CMD [ "yarn", "run", "start" ]  

