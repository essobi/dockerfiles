FROM harmish/node  
  
# install typescript  
RUN npm install -g tslint typescript typings && \  
mkdir -p /workspace/build && \  
#  
# clean-up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /workspace  
WORKDIR /workspace  

