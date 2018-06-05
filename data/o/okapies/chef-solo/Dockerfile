FROM ubuntu:12.04  
MAINTAINER Yuta Okamoto <okapies@gmail.com>  
  
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
build-essential \  
libxml2-dev \  
libxslt-dev && \  
apt-get install -y --no-install-recommends libgecode-dev && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
RUN curl -L https://www.opscode.com/chef/install.sh | bash && \  
echo 'gem: --no-ri --no-rdoc' > ~/.gemrc  
  
# Install berkshelf  
# See https://github.com/opscode/dep-selector-libgecode/issues/15  
RUN USE_SYSTEM_GECODE=1 /opt/chef/embedded/bin/gem install berkshelf  
  
# Clean up  
RUN rm -rf /tmp/* /var/tmp/*  

