FROM ryanratcliff/java8  
MAINTAINER Ryan Ratcliff <ryan.ratcliff@ryanratcliff.net>  
ENV refreshed_at 2015-09-16  
RUN apt-get update && apt-get install -yqq ruby rubygems-integration  
  
RUN gem install fakes3 -v 0.2.1  
  
RUN mkdir -p /data/fakes3  
  
EXPOSE 7070  
ENTRYPOINT ["/usr/local/bin/fakes3"]  
CMD ["-r", "/data/fakes3", "-p", "7070"]  

