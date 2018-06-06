# compass image  
# runs compass within a container  
FROM ubuntu:14.04  
MAINTAINER François Zaninotto <francois+docker@marmelab.com>  
  
ENV HOME /root  
  
RUN apt-get update -qq  
  
# install ruby  
RUN apt-get install -y -qq ruby-dev  
RUN apt-get install -y -qq make  
RUN apt-get install -y -qq ssh  
RUN apt-get install -y -qq rsync  
  
# install compass  
RUN gem install --no-rdoc --no-ri compass  
  
WORKDIR /srv  
  
ENTRYPOINT ["compass"]  

