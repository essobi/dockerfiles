# Run npm within a container  
#  
# docker run -it --rm \  
# -v $HOME/.workspace/node/.npmrc:/root/.npmrc \  
# -v $HOME/.workspace/node/.npm:/root/.npm \  
# -v "$(pwd)"/:/usr/src/app \  
# \--name node \  
# \--entrypoint="$entry" \  
# selfinvoking/node $cmd  
#  
FROM node:4.5  
MAINTAINER Carl Walsh <carl@selfinvoking.com>  
WORKDIR /usr/src/app  
  
RUN echo "export PATH=$PATH:/usr/src/app/node_modules/.bin" >> /root/.bashrc  
  
ENTRYPOINT [ "node" ]  

