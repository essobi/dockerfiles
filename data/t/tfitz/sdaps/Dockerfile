FROM ubuntu:14.04.3  
MAINTAINER Tim Fitzgerald <fitzgeraldt@gonzaga.edu>  
  
RUN apt-get update \  
&& \  
apt-get install -y software-properties-common  
  
RUN add-apt-repository ppa:benjamin-sipsolutions/sdaps  
  
RUN apt-get update && apt-get install -y \  
sdaps  
  
WORKDIR "/workdir"  
  
ENTRYPOINT ["sdaps"]  
  

