FROM debian:sid  
MAINTAINER graham@grahamc.com  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y ats2-lang  
  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["patscc"]  
CMD ["--help"]  
  

