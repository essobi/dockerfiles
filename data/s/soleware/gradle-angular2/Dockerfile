# installing node:6 (nodejs, npm, yarn)  
FROM node:6 as NODE_SOURCE  
  
# installing angular-cli globally  
RUN echo "Installing angular-cli for global use"  
RUN npm install -g @angular/cli@1.4.3  
  
# installing gradle:4.2.1 (java jdk8, gradl 4.2.1)  
FROM gradle:4.2.1-jdk8  
USER root  
  
# check if gradle is properly installed  
RUN echo "Testing gradle installation" && gradle --version  
  
# merge data from previous image  
COPY \--from=NODE_SOURCE /opt/yarn /opt/yarn/  
COPY \--from=NODE_SOURCE /usr/local/lib/node_modules
/usr/local/lib/node_modules/  
COPY \--from=NODE_SOURCE /usr/local/bin /usr/local/bin  
  
# check if node is working properly after merge  
RUN echo "Testing node installation" && node -v && npm -v  
  
# check angular-cli installation  
RUN ng --version  

