#########################################################################  
#  
# A Stombox ember container - used by our API  
#  
# Build with:  
# docker build -t="tuyakhov/stombox-ember" .  
#  
# https://hub.docker.com/_/node/  
#  
########################################################################  
  
# Base from official nodejs image  
FROM node  
  
# Install dependencies  
RUN apt-get update && apt-get install -y git python-dev  
# Install Watchman to improve performance  
RUN git clone https://github.com/facebook/watchman.git  
RUN cd watchman && git checkout v4.5.0 && \  
./autogen.sh && ./configure && \  
make && make install  
########  
# In case of getting error "The user limit on the total number of inotify
watches was reached" need to execute the command below  
# docker run --rm --privileged --entrypoint sysctl tuyakhov/stombox-ember -w
fs.inotify.max_user_watches=16384  
# It is temporary solution. Need to wait for official solution  
########  
#RUN echo fs.inotify.max_user_watches=16384 | tee -a /etc/sysctl.conf &&
sysctl -p  
  
# Install Ember using npm  
RUN npm install -g ember-cli@2.9.1  
RUN npm install -g bower  
RUN npm install -g phantomjs-prebuilt  
  
# Directory of ember application  
VOLUME ["/code"]  
  
WORKDIR /code  
  
EXPOSE 4200 49152  

