FROM ubuntu:15.10  
ENV _FLYWAY_V=3.2.1  
ENV _FLYWAY=flyway-commandline-${_FLYWAY_V}-linux-x64.tar.gz  
  
MAINTAINER Blue Thomas <blue.thomas@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
curl  
  
RUN curl -L https://bintray.com/artifact/download/business/maven/${_FLYWAY} >
${_FLYWAY}  
RUN tar zxvf ${_FLYWAY}  
RUN rm ${_FLYWAY}  
RUN mv flyway-${_FLYWAY_V} flyway  
  
ENV PATH ./flyway:$PATH  
  
CMD flyway -url=jdbc:h2:mem:test_db info  

