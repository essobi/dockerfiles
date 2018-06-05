# Alpine + Angular  
FROM coodoogmbh/docker-angular-cli  
  
MAINTAINER Jan Marsh <jan.marsh@coodoo.de>  
  
ENV AWS_REGION "eu-central-1"  
RUN apk --update --no-cache add curl \  
rm -rf /var/cache/apk/*  
  
# Configure aws  
RUN mkdir /root/.aws && \  
echo "[default]" >> /root/.aws/config \  
echo "region = $AWS_REGION" >> \/root/.aws/config \  
touch /root/.aws/credentials \  
echo "[default]" >> /root/.aws/credentials \  
echo "aws_access_key_id = $AWS_ACCESS_KEY_ID" >> /root/.aws/credentials \  
echo "aws_secret_access_key = $AWS_SECRET_ACCESS_KEY" >>
/root/.aws/credentials \  
chmod 600 ~/.aws/credentials  
  
# Install ecs-cli  
RUN curl --silent -o /usr/local/bin/ecs-cli http://s3.amazonaws.com/amazon-
ecs-cli/ecs-cli-linux-amd64-latest && \  
chmod +x /usr/local/bin/ecs-cli && \  
ecs-cli --version  
  
CMD ["sh"]

