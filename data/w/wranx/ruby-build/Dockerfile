FROM wranx/ruby-runtime:latest  
RUN apt-get update && apt-get install -y ant  
RUN (curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash) && \  
apt-get install -y git-lfs  
RUN apt-get update && \  
apt-get install -y unzip && \  
apt-get install -y python-dev && \  
curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o /tmp/awscli-
bundle.zip && \  
cd /tmp && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN apt-get update && \  
apt-get -y install postgresql  
RUN apt-get update && \  
apt-get -y install jq  
RUN apt-get update && \  
apt-get -y install gettext-base  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev pkg-
config g++ libqt4-dev libqtwebkit-dev xvfb  

