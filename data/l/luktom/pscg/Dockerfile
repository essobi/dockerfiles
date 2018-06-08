FROM mesosphere/aws-cli  
  
VOLUME ["/data"]  
  
RUN apk update && apk add curl tar jq && rm -rf /var/lib/apt/lists*  
  
COPY generate_config /  
  
ENTRYPOINT ["/generate_config"]  
  

