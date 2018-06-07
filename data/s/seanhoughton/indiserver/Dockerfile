FROM ubuntu:xenial  
MAINTAINER Sean Houghton <sean.houghton@gmail.com>  
  
ARG LIBINDI_VERSION=\\*  
ARG INDI_VERSION=\\*  
  
RUN apt-get update && apt-get install -y software-properties-common  
RUN apt-add-repository ppa:mutlaqja/ppa && apt-get update && apt-get install
-y libindi1=${LIBINDI_VERSION} indi-full=${INDI_VERSION}  
  
EXPOSE 7624  
ENTRYPOINT ["indiserver", "-v"]  
CMD ["indi_watchdog", "indi_simulator_ccd", "indi_simulator_dome",
"indi_simulator_telescope"]  

