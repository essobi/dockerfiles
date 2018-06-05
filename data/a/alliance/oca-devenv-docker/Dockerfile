# newer versions of node cause errors :(  
FROM node:boron  
  
# install exlibris devenv and our packages  
WORKDIR /home/node  
COPY package.json .  
RUN npm install  
RUN mv /home/node/node_modules/primo-explore-devenv /home/node/primo-explore-
devenv  
WORKDIR /home/node/primo-explore-devenv  
RUN npm install  
RUN npm rebuild node-sass  
  
# link the default alliance package and central package  
RUN mkdir -p primo-explore/custom/ALLIANCE  
RUN mkdir -p primo-explore/custom/CENTRAL_PACKAGE  
RUN mv /home/node/node_modules/oca-test-package/src/* /home/node/primo-
explore-devenv/primo-explore/custom/ALLIANCE  
RUN mv /home/node/node_modules/oca-central-package/src/* /home/node/primo-
explore-devenv/primo-explore/custom/CENTRAL_PACKAGE  
  
# expose ports  
EXPOSE 8003  
EXPOSE 3001  
# set default proxy and view options  
ENV PROXY "http://alliance-primo-sb.hosted.exlibrisgroup.com:80"  
ENV VIEW ALLIANCE  
  
# run  
CMD [ "/bin/bash", "-c", "node_modules/.bin/gulp run --view $VIEW \--proxy
$PROXY" ]  

