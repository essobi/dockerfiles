# Tinkerpop Rexster Server  
#  
FROM ubuntu  
MAINTAINER Konrad Eriksson "konrad@konraderiksson.com"  
# Install unzip so we later can unpack  
RUN apt-get -y install unzip  
  
# Rexster requires Java 7 to run  
RUN apt-get -y install openjdk-7-jre-headless  
  
ADD http://tinkerpop.com/downloads/rexster/rexster-server-2.5.0.zip /  
  
RUN unzip rexster-server-2.5.0.zip  
RUN rm rexster-server-2.5.0.zip  
RUN mv rexster-server-2.5.0 rexster-server  
  
# Server listening port  
EXPOSE 8182  
# RexPro port  
EXPOSE 8184  
# Shutdown listener port  
EXPOSE 8183  
WORKDIR rexster-server  
  
## Entrypoint  
ENTRYPOINT ["bin/rexster.sh", "--start"]  

