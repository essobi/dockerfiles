FROM node AS build  
  
RUN npm install -g roc@next  
RUN mkdir /src  
WORKDIR /src  
ADD package* /src/  
  
RUN npm install  
  
ADD . /src  
RUN roc build  
  
# FROM node:alpine  
# RUN npm install -g roc  
# COPY roc.config.js /app/roc.config.js  
# COPY --from=build /src/build /app  
# WORKDIR /app  
ENTRYPOINT ["roc"]  
CMD ["start"]  
EXPOSE 3000  

