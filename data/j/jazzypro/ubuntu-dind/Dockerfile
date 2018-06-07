FROM gitlab/dind  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Docker from Docker Inc. repositories.  
# and unzip  
RUN curl -sSL https://get.docker.com/ | sh && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y docker-ce && \  
apt-get install -y unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -s -L https://github.com/docker/compose/releases/latest | \  
egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-
Linux-x86_64' | \  
wget --base=http://github.com/ -i - -O /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
/usr/local/bin/docker-compose --version  
  
#  
# Install AWS CLI  
#  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  

