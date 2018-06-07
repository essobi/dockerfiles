FROM debian:stretch-slim  
  
RUN apt-get update -y && \  
apt-get install -y gnupg git build-essential curl && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 93C4A3FD7BB9C367 &&
\  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list && \  
echo "deb http://packages.cloud.google.com/apt cloud-sdk-stretch main" >>
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
apt-get update -y && \  
apt-get install -y ansible ruby ruby-dev google-cloud-sdk kubectl && \  
gem install test-kitchen kitchen-ssh && \  
gem install kitchen-inspec -v 0.22.0 && \  
git clone https://github.com/kamatama41/tfenv.git /opt/tfenv && \  
ln -s /opt/tfenv/bin/* /usr/local/bin && \  
rm -rf /var/lib/apt/lists/*  

