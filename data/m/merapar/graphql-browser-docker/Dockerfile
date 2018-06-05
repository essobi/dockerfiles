FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y git && apt-get install -y curl  
  
RUN git clone https://github.com/graphql/graphiql.git  
  
WORKDIR /graphiql  
  
RUN git checkout 2cc64d2  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get install -y nodejs  
  
RUN npm install && npm run build  
  
WORKDIR /graphiql/example  
  
RUN sed -i -e "s|credentials|//credentials|g" index.html  
  
RUN npm install  
  
EXPOSE 8080  
COPY run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
ENTRYPOINT /run.sh  

