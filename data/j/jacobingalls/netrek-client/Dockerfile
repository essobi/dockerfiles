FROM ubuntu  
  
MAINTAINER Jacob Ingalls <jacobingalls@yahoo.com>  
  
RUN apt-get update \  
&& apt-get install -y -f netrek-client-cow \  
&& apt-get autoremove && apt-get clean  
  
CMD /usr/games/netrek-client-cow  

