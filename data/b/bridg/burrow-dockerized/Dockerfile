FROM bridg/burrow  
  
RUN apk update \  
&& apk --no-cache add ca-certificates openssl \  
&& update-ca-certificates  
  
ENV DOCKERIZE_VERSION v0.3.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
COPY ./config/burrow /etc/burrow  
  
ENTRYPOINT ["dockerize", "-template",
"/etc/burrow/templates/burrow.tmpl:/etc/burrow/burrow.cfg"]  
CMD ["/go/bin/burrow", "--config", "/etc/burrow/burrow.cfg"]  

