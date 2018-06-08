FROM phusion/baseimage:latest  
  
MAINTAINER Pedro César "pedrocesar@uppoints.com"  
ENV SETUP_DIR /tmp/deploy/  
  
ADD deploy/ ${SETUP_DIR}  
  
#ADD https://s3.amazonaws.com/puppet.uppoints.com/modules_repository.tgz
${SETUP_DIR}  
#RUN tar -xzvf ${SETUP_DIR}/modules_repository.tgz -C ${SETUP_DIR}  
RUN apt-get update\  
&& apt-get install -y wget unzip\  
&& wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb\  
&& dpkg -i puppetlabs-release-pc1-xenial.deb\  
&& apt-get update\  
&& apt-get -y install puppet\  
&& wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -O awscli-
bundle.zip\  
&& unzip awscli-bundle.zip\  
&& sed -i 's/\/usr\/bin\/env\ python/\/usr\/bin\/env\ python3/g' ./awscli-
bundle/install\  
&& ./awscli-bundle/install -b /sbin/aws\  
&& puppet apply --modulepath=${SETUP_DIR} -e "class {'upp_repository': }"\  
&& rm -rf ${SETUP_DIR} awscli-bundle* puppetlabs-release-pc1-xenial.deb  
  
VOLUME ["/var/cache/repository"]  
CMD ["/sbin/my_init"]

