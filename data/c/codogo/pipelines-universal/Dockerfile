FROM ubuntu:latest  
  
MAINTAINER hootiebrown@codogo.io  
  
#installing cURL  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y curl  
  
#add apt-get node/npm  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
#add apt-get yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
#add apt-get git lfs  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash  
  
#install apt-get  
RUN apt-get update  
RUN apt-get install -y \  
build-essential \  
gcc \  
git-lfs \  
imagemagick \  
jq \  
make \  
nodejs \  
python3-software-properties \  
python-dev \  
python-pip \  
python-software-properties \  
ruby \  
ruby-dev \  
software-properties-common \  
tree \  
yarn  
  
#install aws cli  
RUN pip install awscli  
RUN aws configure set preview.cloudfront true  
  
#install jekyll  
RUN gem install jekyll --no-rdoc --no-ri -v 3.2.1  
RUN gem install bundler  
RUN gem cleanup  
  
#install serverless  
RUN npm install -g serverless  
  
#install react-native  
RUN npm install -g react-native-cli  
  
#install codepush  
RUN npm install -g code-push-cli  
  
#install codepush  
RUN npm install -g graphcool@next  

