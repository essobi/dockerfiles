FROM node:alpine  
LABEL maintainer="russleyshaw@gmail.com"  
  
RUN apk --no-cache add python make gcc alpine-sdk  
  
ADD . app  
WORKDIR app  
  
RUN npm run setup  
RUN npm run build  
  
EXPOSE 80  
CMD ["npm", "run", "start-prod"]  

