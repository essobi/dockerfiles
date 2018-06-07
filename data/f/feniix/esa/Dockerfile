FROM ubuntu:14.04.1  
MAINTAINER Gary Turovsky "gary@spantree.net"  
RUN apt-get -y update  
RUN apt-get -y install ruby-dev git build-essential  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN gem install puppet -v3.6.2 && gem install librarian-puppet -v1.0.9  
  
ADD puppet/hiera.yaml /etc/puppet/  
ADD puppet /puppet  
  
WORKDIR /puppet  
  
RUN librarian-puppet install  
  
ENV FACTER_LSBDISTID debian  
  
RUN puppet apply --verbose --debug --modulepath=modules manifests/default.pp  
  
# Define working directory.  
WORKDIR /data  
  
VOLUME ["/data"]  
  
# Define default command.  
CMD ["/usr/share/elasticsearch/bin/elasticsearch",
"-Des.config=/etc/elasticsearch/elasticsearch.yml"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  
EXPOSE 54328  

