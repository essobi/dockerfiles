FROM ubuntu:14.04.5  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN apt-get update && apt-get -y install curl  
RUN (curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash) && \  
apt-get install -y git-lfs  
RUN apt-get update && \  
apt-get install -y ant  
RUN apt-get update && \  
apt-get install -y unzip && \  
apt-get install -y python-dev && \  
curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o /tmp/awscli-
bundle.zip && \  
cd /tmp && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN apt-get update && \  
apt-get -y install jq  
RUN apt-get update && \  
apt-get -y install gettext-base  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && \  
sudo apt-get install -y nodejs  
RUN npm install -g s3-website  
RUN curl -L https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-3.1.0.1141-linux.zip -o /opt/sonar-scanner.zip && \  
cd /opt && \  
unzip sonar-scanner.zip && \  
ln -s sonar-scanner-3.1.0.1141-linux sonar-scanner && \  
rm sonar-scanner.zip  

