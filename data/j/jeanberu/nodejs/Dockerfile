FROM alpine:3.2  
RUN mkdir /src \  
&& apk add --update nodejs \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
WORKDIR /src  
  
CMD ["node"]  

