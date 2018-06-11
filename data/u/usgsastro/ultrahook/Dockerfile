FROM ruby:2.3  
MAINTAINER rbogle@usgs.gov  
RUN gem install ultrahook  
  
ADD ./ultrahook.bash /usr/bin/  
  
ENTRYPOINT ["/usr/bin/ultrahook.bash"]  

