FROM ubuntu:14.04.4  
ENV PATH=/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
  
ENV PUPPET_RELEASE trusty  
ENV R10K_VERSION='2.2.0'  
# Install puppet-agent and git  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -O http://apt.puppetlabs.com/puppetlabs-release-
pc1-${PUPPET_RELEASE}.deb \  
&& dpkg -i puppetlabs-release-pc1-${PUPPET_RELEASE}.deb \  
&& apt-get update \  
&& apt-get install -y puppet-agent git \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install r10k  
RUN gem install r10k --version $R10K_VERSION \--no-ri --no-rdoc  
  
# Configure .ssh directory  
RUN mkdir /root/.ssh \  
&& chmod 0600 /root/.ssh \  
&& echo StrictHostKeyChecking no > /root/.ssh/config  
  
# Configure volumes  
VOLUME ["/opt/puppetlabs/r10k/cache/", "/etc/puppetlabs/code"]  
  
# Configure entrypoint  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
RUN chmod 755 /docker-entrypoint.sh && chmod -R 755 /docker-entrypoint.d  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

