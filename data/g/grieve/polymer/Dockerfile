FROM node:latest  
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>  
  
RUN npm install -g \  
polybuild \  
polyserve \  
polylint \  
polymer-cli  
  
VOLUME ["/src"]  
  
CMD ["polyserve", "/src"]

