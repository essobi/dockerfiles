FROM buildpack-deps:jessie-scm  
  
RUN apt update \  
&& apt -qq install -y --no-install-recommends \  
clang \  
make \  
cmake  
  
RUN wget https://github.com/philsquared/Catch/archive/v1.10.0.tar.gz \  
&& tar -zxvf v1.10.0.tar.gz \  
&& mkdir /usr/local/include/catch \  
&& cp -rf Catch-1.10.0/include/* /usr/local/include/catch/  
  

