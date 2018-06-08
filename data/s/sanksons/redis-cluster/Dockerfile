FROM redis:3.0  
  
MAINTAINER sanksons <glitter.sankalp@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#############################  
# Install required plugins  
#############################  
RUN apt-get update  
RUN apt-get --assume-yes install wget ruby ruby-dev gem  
WORKDIR /tmp  
RUN wget http://production.cf.rubygems.org/rubygems/rubygems-update-2.0.3.gem  
RUN gem install rubygems-update-2.0.3.gem  
RUN update_rubygems  
RUN gem install --no-ri --no-rdoc redis  
WORKDIR /  
#######################  
# Copy Build Files  
#######################  
RUN mkdir /buildfiles  
COPY Dockerfile buildfiles/Dockerfile  
COPY create-cluster buildfiles/create-cluster  
COPY redis-trib.rb buildfiles/redis-trib.rb  
  
RUN mkdir /rediscluster  
COPY create-cluster rediscluster/create-cluster  
COPY redis-trib.rb /usr/local/bin/redis-trib.rb  
  
WORKDIR /rediscluster  
#ENTRYPOINT ["./create-cluster", "start"]  
#CMD ["./create-cluster", "create"]  
CMD ./create-cluster start && ./create-cluster create && (while :; do echo
'Hit CTRL+C'; sleep 100; done)  
  
  

