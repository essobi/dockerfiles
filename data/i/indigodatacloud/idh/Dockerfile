FROM ubuntu:trusty  
  
MAINTAINER KIT-SCC  
  
# Install prerequisites  
RUN apt-get update  
RUN apt-get install -y software-properties-common git  
  
# Install java8  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
# Install maven  
RUN apt-get install -y maven  
  
# Clone and build  
RUN git clone https://github.com/indigo-dc/identity-harmonization.git  
RUN cd identity-harmonization && \  
git pull && \  
mvn clean package  
  
ENTRYPOINT ["/identity-harmonization/target/identity-harmonization-2.0.jar"]  
#CMD ["--server.port=8080 --cdmi.data.baseDirectory=/data"]  
# Expose data folder and port  
EXPOSE 8443  

