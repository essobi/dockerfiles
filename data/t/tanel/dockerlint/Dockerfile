FROM node:4-alpine  
  
ENV DOCKERLINT_VERSION="0.3.9"  
RUN npm -g install dockerlint && rm -rf /root/.npm  
  
ENTRYPOINT ["dockerlint", "/Dockerfile"]  

