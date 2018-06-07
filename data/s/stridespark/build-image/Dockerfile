FROM circleci/node:8.6.0  
#These two commands allow us to install postgres-client-10 event though only
9.3 is available on trusty  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
sudo apt-key add -  
  
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list'  
  
#Go install some stuff  
RUN sudo apt-get -y -qq update && \  
sudo apt-get -y -qq install \  
python-pip \  
python-dev \  
build-essential \  
postgresql-client-10 \  
mysql-client \  
apt-transport-https \  
software-properties-common \  
jq \  
rsync \  
&& sudo rm -rf /var/lib/apt/lists/*  
  
#Go add docker-ce to apt-get repo and then install  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add
- && \  
sudo add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable" && \  
sudo apt-get update && \  
sudo apt-get -y -qq install docker-ce && \  
sudo rm -rf /var/lib/apt/lists/*  
  
#Install pipsi, then use pipsi to install awscli and credstash  
RUN sudo pip install pipsi==0.9  
RUN sudo pipsi --home=/ --bin-dir=/bin install awscli==1.11.165  
RUN sudo pipsi --home=/ --bin-dir=/bin install credstash==1.14.0  
  
#Install kubectl  
RUN sudo wget --progress=dot:mega https://storage.googleapis.com/kubernetes-
release/release/v1.6.2/bin/linux/amd64/kubectl && sudo chmod +x kubectl &&
sudo mv kubectl /usr/local/bin  
  
#Install yarn  
RUN sudo npm install -g yarn@1.3.2  
  
ADD circle.npmrc /home/circleci/.npmrc  
ADD circle.npmrc /usr/local/share/.npmrc  
  
ENV AWS_DEFAULT_REGION="us-west-2"  
ENV PGHOST="localhost"  
ENV PGUSER="postgres"  
ENV BASH_ENV="/app/bash.env"  
# use staging snowflake schema by default for build image  
ENV USE_STAGING="true"  
ENV NODE_ENV="test"  
RUN sudo mkdir /app && sudo chown circleci:circleci app

