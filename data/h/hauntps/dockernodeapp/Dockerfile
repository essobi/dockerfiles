FROM mhart/alpine-node:latest  
  
WORKDIR /src/app  
  
COPY ./MyWeb/package.json /src/app/  
  
RUN yarn && mkdir /src/logs  
  
COPY ./MyWeb/ /src/app/  
  
EXPOSE 3000 80  
ENTRYPOINT ["./entry.sh"]

