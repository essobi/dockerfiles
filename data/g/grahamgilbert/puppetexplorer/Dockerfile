FROM alpine:3.1  
COPY puppetexplorer /puppetexplorer  
WORKDIR /puppetexplorer  
RUN apk add --update nodejs  
RUN apk --update add --virtual build-dependencies build-base git \  
&& npm install \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
RUN npm install -g grunt-cli napa  
RUN grunt  
RUN sed -i '/hostname/s/localhost/0.0.0.0/' Gruntfile.coffee  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

