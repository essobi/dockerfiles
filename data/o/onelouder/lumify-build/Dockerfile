FROM ubuntu:16.04  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get -y update \  
&& apt-get -y install \  
software-properties-common \  
apt-transport-https \  
curl \  
ca-certificates \  
# Install Java  
&& add-apt-repository \  
ppa:webupd8team/java \  
# Install Docker  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" \  
&& apt-get -y update \  
&& apt-get -y install \  
oracle-java8-installer \  
maven \  
git-core \  
zlib1g-dev \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
python-software-properties \  
libffi-dev \  
nodejs \  
ruby-dev \  
python-pip \  
python-dev \  
docker-ce  
RUN gem install --no-ri --no-rdoc \  
deep_merge \  
trollop \  
chef-api  
RUN pip install \  
s3cmd \  
docker-compose  

