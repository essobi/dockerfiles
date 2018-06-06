FROM ubuntu:latest  
MAINTAINER byteshiva <byteshiva@gmail.com>  
  
# Set locale to avoid apt-get warnings in OSX  
RUN locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
ENV LC_ALL C  
ENV LC_ALL en_US.UTF-8  
# Install chef and its prerequisites  
# NOTE: libgecode-dev required by dep-selector-libgecode in berfshelf  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
curl \  
git \  
ruby \  
wget \  
build-essential \  
libxml2-dev \  
libxslt-dev && \  
apt-get install -y --no-install-recommends libgecode-dev && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN wget --no-check-certificate -O ruby-install-0.6.0.tar.gz
https://github.com/postmodern/ruby-install/archive/v0.6.0.tar.gz  
RUN tar -xzvf ruby-install-0.6.0.tar.gz  
# RUN cd ruby-install-0.6.0/  
# \ sudo make install  
# \ ruby-install --latest ruby  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -L get.rvm.io | bash -s stable  
RUN find / -name "rvm.sh"  
# RUN find / -name "rvm.sh" | xargs source  
RUN source /etc/profile.d/rvm.sh  
# source /etc/profile.d/rvm.sh  
# RUN rvm reload  
RUN rvm install 2.3.0  
RUN rvm use 2.3.0 --default  
  
# Run the installer  
# RUN bash rvm-installer stable  
# RUN rvm install 2.3.0  
# RUN \rvm use 2.3.0 --default  
RUN gem install chef-zero  
RUN wget --no-check-certificate
https://packages.chef.io/stable/ubuntu/12.04/chefdk_0.11.2-1_amd64.deb  
RUN dpkg -i chefdk_0.11.2-1_amd64.deb  

