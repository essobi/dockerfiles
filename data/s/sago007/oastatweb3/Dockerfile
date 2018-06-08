FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y libcppdb-dev libctemplate-dev build-
essential gnuplot git wget cmake libpcre3-dev zlib1g-dev libgcrypt11-dev
libicu-dev python libboost-dev  
  
RUN mkdir -p /opt/oastatweb/  
  
RUN cd /opt/ && wget
https://files.poulsander.com/~poul19/public_files/cppcms-1.0.5.tar.bz2 && tar
xvfj cppcms-1.0.5.tar.bz2 && mkdir -p cppcms-1.0.5/build && cd
cppcms-1.0.5/build && cmake .. && make && make install  
  
RUN cd /opt/oastatweb/ && git clone https://github.com/sago007/OaStatWeb3.git
&& cd OaStatWeb3 && make && ldconfig && chmod o+w ./media && echo changed  
  
EXPOSE 27960  
USER nobody  
  
WORKDIR /opt/oastatweb/OaStatWeb3  
  
CMD ./OaStatWeb3 -c docker/config-docker.js  

