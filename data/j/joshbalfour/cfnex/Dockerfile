FROM mhart/alpine-node  
  
ADD . /src  
  
RUN cd /src && npm install -g . --production  
  
ENTRYPOINT ["cfnex"]

