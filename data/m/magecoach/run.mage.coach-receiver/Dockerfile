FROM mhart/alpine-node:6  
MAINTAINER Ray Bogman <bogman@bogman.info>  
  
RUN apk add --no-cache make git gcc g++ python bash && rm -rf /var/cache/apk/*  
RUN npm install -g node-gyp\  
&& ln -s $(which node-gyp) $(dirname $(which node-gyp))/node-gyp\  
&& npm cache clear\  
&& node-gyp configure || echo ""  
## replaces git clone. for quick dev, use COPY of local files  
#COPY ./scripts/ /home/root/scripts  
#COPY ./receiver /receiver  
#RUN cd /receiver && \  
# npm install -g  
## Install receiver code  
RUN git clone https://github.com/magecoach/run.mage.coach.git && \  
cd run.mage.coach/receiver/ && \  
npm install -g && \  
npm cache clean  
  
ENV LOG_FILE /var/log/mage.coach/receiver.log  
  
ENTRYPOINT ["/home/root/scripts/start.sh"]  

