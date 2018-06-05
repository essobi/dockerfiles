FROM ubuntu  
MAINTAINER Jignesh Sheth "jsheth@pivotal.io"  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# make sure the package repository is up to date  
RUN apt-get update  
RUN apt-get install -y wget curl build-essential git-all jq vim ruby ruby-dev
libxml2-dev libsqlite3-dev libxslt1-dev libpq-dev libmysqlclient-dev
zlib1g-dev nodejs npm default-jre default-jdk  
RUN apt-get update  
  
# Install CF CLI  
RUN wget -O 'cf.deb' https://s3.amazonaws.com/pcf-softwares-57/cf-cli-
installer_6.32.0_x86-64.deb  
RUN dpkg --install cf.deb  
RUN rm cf.deb  
RUN cf install-plugin https://github.com/bluemixgaragelondon/cf-blue-green-
deploy/releases/download/v1.2.0/blue-green-deploy.linux64 -f  
RUN cf plugins  
  
# Install UAA CLI  
RUN gem install cf-uaac  
  
# Install Azure CLI  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g azure-cli  
RUN azure --version  
  
# Install Ops Manager CLI tool  
RUN wget -O '/usr/local/bin/om' https://github.com/pivotal-
cf/om/releases/download/0.27.0/om-linux  
RUN chmod 755 /usr/local/bin/om  
  
# Install Pivnet CLI  
RUN wget -O '/usr/local/bin/pivnet' https://github.com/pivotal-cf/pivnet-
cli/releases/download/v0.0.49/pivnet-linux-amd64-0.0.49  
RUN chmod 755 /usr/local/bin/pivnet  
  
# Install Credhub CLI  
RUN wget -O 'credhub.tgz' https://github.com/cloudfoundry-incubator/credhub-
cli/releases/download/1.5.0/credhub-linux-1.5.0.tgz  
RUN tar xvfz credhub.tgz && mv credhub /usr/local/bin  
  
# Install BOSH CLI  
RUN wget -O '/usr/local/bin/bosh' https://s3.amazonaws.com/bosh-cli-
artifacts/bosh-cli-2.0.44-linux-amd64  
RUN chmod 755 /usr/local/bin/bosh  

