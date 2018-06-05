FROM docker:17  
RUN apk add --no-cache py-pip  
RUN apk add --no-cache curl  
RUN apk add --no-cache jq  
RUN pip install docker-compose  
RUN pip install awscli  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest  
RUN chmod +x /usr/local/bin/ecs-cli  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

