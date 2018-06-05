FROM ruby  
  
# installs bundler  
RUN gem install bundler  
  
# basics  
RUN apt-get update && \  
apt-get -y install \  
libmysqlclient-dev \  
libidn11-dev \  
vim  
  
ENTRYPOINT ["bundle"]  

