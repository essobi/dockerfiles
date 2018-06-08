#A lightweight node image  
FROM mhart/alpine-node:9.6.0  
  
#PM2 will be used as PID 1 process  
#RUN npm install -g pm2@1.1.3  
RUN npm install pm2 -g  
  
# Copy package json files for services  
  
COPY ./package.json /var/www/package.json  
  
# Set up working dir  
WORKDIR /var/www  
  
# Install packages  
RUN npm config set loglevel warn \  
# To mitigate issues with npm saturating the network interface we limit the
number of concurrent connections  
&& npm config set maxsockets 5 \  
&& npm config set only production \  
&& npm config set progress false \  
&& npm i  
  
  
# Copy source files  
COPY . ./  
  
# Expose ports  
EXPOSE 5000  
  
# Start PM2 as PID 1 process  
# ENTRYPOINT ["pm2", "--no-daemon", "start"]  
# Actual script to start can be overridden from `docker run`  
# CMD ["process.config.js"]  
CMD pm2 start --no-daemon process.config.js  
# CMD ["pm2-runtime", "process.js", "--json"]

