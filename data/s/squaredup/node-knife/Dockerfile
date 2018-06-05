FROM node:latest  
  
RUN apt-get update -qqy && \  
apt-get -qqy install curl  
  
RUN curl https://omnitruck.chef.io/install.sh | bash -s -- -P chefdk -v 0.10.0  
  
# This sucks but it's the simplest way to appease knife plugins etc. and have
them work  
#  
env PATH /root/.chefdk/gem/ruby/2.1.0/bin:$PATH  
  
RUN chef gem install knife-push  
RUN chef gem install knife-attribute  
RUN chef gem install knife-reporting  
RUN chef gem install knife-azure  
  
CMD [ "node" ]

