FROM openjdk:8  
RUN apt-get update \  
&& apt-get install --yes \  
ant \  
build-essential \  
git \  
python  
  
RUN git clone https://github.com/facebook/buck.git  
  
WORKDIR /buck  
  
RUN ant \  
&& ln -s ${PWD}/bin/buck /usr/local/bin/buck \  
&& ln -s ${PWD}/bin/buckd /usr/local/bin/buckd  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  

