FROM ubuntu:16.04  
RUN apt-get update -qqy && \  
apt-get -qqy install curl  
  
RUN curl https://omnitruck.chef.io/install.sh | bash -s -- -P chefdk -v 1.4.3  
  
RUN chef gem install knife-push  
  
# Expected to contain only .chef with knife.rb and the required PEM  
ENV CHEF_REPO_STUB "/repo"  
ENV JOB_COMMAND "job start \"chef-client\""  
CMD cd ${CHEF_REPO_STUB} && knife ${JOB_COMMAND}

