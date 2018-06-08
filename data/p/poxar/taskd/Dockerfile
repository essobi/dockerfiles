  
#  
# taskd  
#  
# Builds a basic docker image that can run taskd  
#  
FROM debian:stable  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get \--yes update \  
&& apt-get \--yes upgrade \  
&& apt-get \--yes install \  
curl \  
build-essential \  
cmake \  
libcurl4-gnutls-dev \  
uuid-runtime \  
uuid-dev  
  
RUN curl "http://taskwarrior.org/download/taskd-1.0.0.tar.gz" -o taskd.tar.gz  
RUN tar zxf taskd.tar.gz  
RUN rm taskd.tar.gz  
  
RUN cd taskd-1.0.0 \  
&& cmake -DCMAKE_BUILD_TYPE=release . \  
&& make install  
  
VOLUME ["/data"]  
CMD ["taskd", "server", "--data", "/data"]  
  

