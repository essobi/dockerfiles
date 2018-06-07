FROM node:9.8.0-alpine  
  
LABEL maintainer="Roman Tarnavski"  
  
RUN apk add --update \  
git  
  
WORKDIR /app  
  
RUN git clone https://github.com/romant/dingo.git .  
  
# build thy lovely app  
RUN npm install  
  
ENV PORT=80  
EXPOSE 80  
CMD npm run serve

