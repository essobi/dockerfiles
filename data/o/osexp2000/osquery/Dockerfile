FROM ubuntu:xenial  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-get install apt-transport-https  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
1484120AC4E9F8A1A577AEEE97A80C63C9D8B80B \  
&& add-apt-repository "deb [arch=amd64] https://osquery-
packages.s3.amazonaws.com/xenial xenial main" \  
&& apt-get update \  
&& apt-get install -y osquery \  
&& rm -rf /var/lib/apt/lists/*  

