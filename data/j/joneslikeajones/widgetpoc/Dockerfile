# We will start with the official base image of Node  
# This is because it comes with Node & NPM ready to go (almost)  
# The `argon` bit means to grab the Node image that has the LTS version  
FROM node:argon  
  
# Next, let's update NPM  
# It's not pretty, but it works  
RUN npm --user root --unsafe-perm true install npm -g  
  
# Now, our application will have a `package.json` that defines packages  
# Let's go ahead and grab that so we can install some packages  
# [1] This section is a bit strange looking at first, it is explained below  
ADD package.json /tmp/package.json  
  
# Then, we can move to the `/tmp` directory and install our packages  
RUN cd /tmp && npm install  
  
# Our packages are installed, but they aren't much use to us in `/tmp`  
# Let's move them to our application directory  
# (creating it if it doesn't exist)  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
# Now we'll change our working directory  
WORKDIR /usr/src/app  
  
# And finally add all our files from our host machine  
ADD . /usr/src/app  
  
# I'm also going to expose a port here, we'll use this later  
EXPOSE 8080  
# Finally, we'll run a command whenever we start this in a container  
CMD ["npm", "run", "dev"]  

