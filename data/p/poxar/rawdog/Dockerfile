  
#  
# rawdog  
#  
# Builds a basic docker image that can run rawdog  
#  
FROM debian:stable  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qqy update \  
&& apt-get -qqy upgrade \  
&& apt-get -qqy install rawdog  
  
VOLUME ["/config"]  
VOLUME ["/html"]  
CMD ["/usr/bin/rawdog", "-uw", "-d", "/config"]  
  

