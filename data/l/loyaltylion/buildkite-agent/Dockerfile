FROM buildkite/agent:2.6  
ENV AWS_DEFAULT_REGION eu-west-1  
RUN apk add --update --no-cache parallel openssl  
RUN pip install awscli  
RUN pip install -U pip docker-compose==1.13.0  
  
RUN curl -sLo /usr/bin/docker-credential-ecr-login \  
https://loyaltylion-static.s3.amazonaws.com/docker/docker-credential-ecr-login
\  
&& chmod +x /usr/bin/docker-credential-ecr-login  
  
RUN mkdir -p /root/.docker && \  
echo '{ "credsStore": "ecr-login" }' > /root/.docker/config.json  
  
ADD hooks /buildkite/hooks/  

