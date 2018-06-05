FROM node:8.1.4-alpine  
# if there are any problems with using alpine, you can remove the `-alpine`
from the former line.  
# (this will at least double the size of the resulting image)  
# this also requires the following changes:  
# * remove the lines for the next three **layers** from the docker file  
# bash is not required, it is just to allow runing scripts as we did before in
circle.yml  
# git allowes to pull dependencies from git repos directly (using git urls)  
RUN apk add --update bash git  
# make sure yarn is avalable for usage in build scripts (and print location
and version)  
RUN which yarn && yarn --version;  
  
# all following packages are there to support yarn/node-gyp with building
canvas see test last line  
RUN apk add --update cairo cairo-dev g++ make rsync openssh  
  
RUN mkdir -p /src/  
WORKDIR /src/  
  
RUN yarn global add node-sass  
  
# for developing this file, testing that yarn can install canvas locally by
installing it globally  
# RUN yarn global add canvas@1.6.4 --exact;  

