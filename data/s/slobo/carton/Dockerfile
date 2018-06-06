FROM perl:5.20.2  
MAINTAINER Slobodan Miskovic slobodan@miskovic.ca  
  
# This is a dead-simple container adding Carton to the official perl build,  
# which builds from debian rather than ubuntu. This perl is unthreaded.  
RUN cpanm MIYAGAWA/Carton-v1.0.19.tar.gz && rm -vrf /root/.cpanm  

