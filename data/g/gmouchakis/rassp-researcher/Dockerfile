FROM r-base  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk git maven r-cran-rjava r-cran-gridbase
r-cran-gridextra r-cran-gtable libcurl4-openssl-dev libssl-dev && \  
git clone https://bitbucket.org/dataengineering/rassp.git && cd rassp && mvn
clean install && mvn dependency:copy-dependencies && \  
apt-get --purge remove -y git maven && apt-get --purge autoremove -y && apt-
get clean && rm -rf /var/lib/apt/lists/*  
  
COPY build.R /rassp/RStats/  
  
COPY truststore.jks /root/truststore.jks  
  
COPY application.conf /root/application.conf  
  
COPY conf.sh /usr/bin  
  
RUN cd /rassp/RStats/ && R --no-save < build.R  
  
WORKDIR /rassp/RStats/  
  
CMD conf.sh && R  

