FROM node:8-alpine  
RUN apk update && apk upgrade && apk add --no-cache git bash  
RUN git clone https://github.com/graphql/graphiql.git  
WORKDIR /graphiql  
RUN npm install && npm run build  
WORKDIR /graphiql/example  
RUN sed -i -e "s|credentials|//credentials|g" index.html  
RUN npm install  
EXPOSE 8080  
COPY server.js /graphiql/example  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
ENTRYPOINT /run.sh  

