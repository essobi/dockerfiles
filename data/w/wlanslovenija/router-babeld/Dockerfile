FROM tozd/runit:ubuntu-xenial  
  
RUN apt-get update -q -q && apt-get install iproute2 babeld --yes --force-yes  
  
COPY ./etc /etc  
  

