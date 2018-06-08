FROM maven:3.5.2-jdk-8-slim  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
zsh \  
xmlstarlet \  
unzip \  
python \  
git \  
jq \  
make  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && rm -rf
./awscli-bundle/install  
COPY mvn-version.sh /usr/bin  
RUN chmod +x /usr/bin/mvn-version.sh  
COPY ecr-repo-uri.sh /usr/bin  
RUN chmod +x /usr/bin/ecr-repo-uri.sh  
RUN mkdir -p /mnt/code  
WORKDIR /mnt/code  

