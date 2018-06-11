# Usage:  
# touch "~/.config/configstore/wunderline.json"  
# docker run --rm -it \  
# -v "/etc/localtime:/etc/localtime:ro" \  
# -v "/mydata/wunderline:/root/.config/configstore/"  
# wunderline  
#  
# Known issues: you need to mount wunderline.json in an folder and not as an  
# individual file since wunderline tries to rename it  
  
FROM node:alpine  
  
RUN npm install -g wunderline && \  
rm -rf /root/.gnupg && \  
rm -rf /root/.config && \  
rm -rf /root/.npm && \  
rm -rf /tmp/*  
RUN mkdir -p /root/.config/configstore  
  
  
ENTRYPOINT ["/usr/local/bin/wunderline"]  

