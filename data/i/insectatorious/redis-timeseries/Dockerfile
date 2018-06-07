FROM redis:4  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get install -y wget unzip git cmake  
  
RUN cd /tmp \  
&& git clone \--recursive https://github.com/danni-m/redis-timeseries /redis-
timeseries \  
&& cd /redis-timeseries/src \  
&& make  
  
RUN apt-get purge -y wget unzip git cmake \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
USER redis  
  
CMD ["redis-server", \  
"--appendonly", \  
"yes", \  
"--loadmodule", \  
"/redis-timeseries/src/redis-tsdb-module.so"]  
  

