FROM node:6-slim  
MAINTAINER shufo  
  
RUN npm install -g elm && \  
elm package install -y  
ENV LANG=en_US.UTF-8  
ENTRYPOINT ["elm"]  
CMD ["--help"]  

