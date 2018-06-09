FROM node:9.4.0-slim  
LABEL eiabea <developer@eiabea.com>  
  
# Using slim image and installing these dependencies manually results in a
smaller image  
RUN apt-get update -q && apt-get install --no-install-recommends -q -y \  
python \  
make \  
g++ \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NODE_PATH=/root/node_modules  
ARG NODE_ENV=dev  
ENV NODE_ENV ${NODE_ENV}  
  
COPY ./package.json /root/package.json  
WORKDIR /root  
RUN npm -q install && npm cache clean --force  
  
WORKDIR /src  
COPY . /src  
  
# Default Docker environment  
CMD [ "npm", "start" ]  

