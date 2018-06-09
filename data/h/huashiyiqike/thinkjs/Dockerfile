# from huashiyiqike/nodejs  
# from node:8  
from keymetrics/pm2:8  
# RUN npm i -g think-cli --cache=/tmp/cache && rm -r /tmp/cache  
RUN mkdir -p /src  
ADD src /src  
WORKDIR /src/  
  
RUN tar xJf /src/node_modules.tar && rm /src/node_modules.tar  
  
CMD ["echo", "thinkjs"]

