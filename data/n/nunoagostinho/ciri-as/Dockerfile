FROM ubuntu  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y perl  
  
ENV SW=/root/software  
WORKDIR ${SW}  
  
ADD CIRI .  
ADD CIRI-AS .

