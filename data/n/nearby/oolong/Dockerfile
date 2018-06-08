FROM node:6  
MAINTAINER nearby messaging  
COPY ./ /usr/src/app  
WORKDIR /usr/src/app  
ENV NODE_ENV=staging  
RUN ["npm","install"]  
EXPOSE 3000  
EXPOSE 3001  
CMD ["npm", "start"]

