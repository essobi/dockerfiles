FROM docker:18.03.0-ce  
  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
RUN apk add --no-cache \  
git \  
openssh-client \  
ca-certificates \  
curl \  
unzip \  
python && \  
# aws-cli  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -rf ./awscli-bundle && \  
# ecs-cli  
curl -o /usr/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-
linux-amd64-v1.4.2 && \  
chmod +x /usr/bin/ecs-cli  

