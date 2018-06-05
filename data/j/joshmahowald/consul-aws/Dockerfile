FROM consul:0.7.2  
#ENV CONSUL_HTTP_URL ""  
#ENV CONSUL_SERVER_IP ""  
RUN apk add --no-cache -U jq  
  
COPY consul_join.sh /usr/local/bin  
ENTRYPOINT /usr/local/bin/consul_join.sh  
  
CMD ""  
#CMD ["agent", "-join", "$CONSUL_SERVER_IP"]  

