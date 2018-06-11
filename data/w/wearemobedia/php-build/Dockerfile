FROM wearemobedia/php-fpm:1.1.0  
#Install Core Build  
RUN apt-get update && apt-get install -y curl \  
software-properties-common \  
python3-software-properties && \  
update-alternatives --install /usr/bin/python python /usr/bin/python3.5 1  
RUN (curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash) && \  
apt-get install -y git-lfs  
RUN mkdir -p /usr/share/man/man1  
RUN apt-get update && \  
apt-get install -y ant  
RUN apt-get update && \  
apt-get install -y unzip && \  
apt-get install -y python3-dev && \  
curl -L https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o /tmp/awscli-
bundle.zip && \  
cd /tmp && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm awscli-bundle.zip  
RUN apt-get update && \  
apt-get -y install jq  
RUN apt-get update && \  
apt-get -y install gettext-base  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs  
RUN npm install -g s3-website  
RUN curl -L https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-3.1.0.1141-linux.zip -o /opt/sonar-scanner.zip && \  
cd /opt && \  
unzip sonar-scanner.zip && \  
ln -s sonar-scanner-3.1.0.1141-linux sonar-scanner && \  
rm sonar-scanner.zip  
  
#Install PHP build additional  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

