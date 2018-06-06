FROM node:6  
MAINTAINER jayro salgado  
COPY ./ /usr/src/app  
WORKDIR /usr/src/app  
ENV MYKEY=CHANGED  
RUN ["npm","install"]  
EXPOSE 80  
CMD ["npm", "start"]

