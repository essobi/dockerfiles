FROM node:4.7.3  
ENV NPM_CONFIG_LOGLEVEL info  
RUN mkdir /workdir && chown -R node workdir  
WORKDIR /workdir  
RUN apt-get update && apt-get install python-dev musl-dev -y \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli  
# RUN apk add --update git python python-dev py-pip musl-dev build-base curl \  
#&& curl -O https://bootstrap.pypa.io/get-pip.py \  
#&& python get-pip.py \  
#&& pip install awscli  
Run npm i backstopjs node-sass bower -g  
USER node  
# CMD ["npm", "i", "--silent"]  
CMD ["npm", "i"]  

