FROM maven  
  
#Needed to add key for cf-cli  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apt-transport-https  
  
#Install cf-cli  
#https://docs.cloudfoundry.org/cf-cli/install-go-cli.html  
RUN wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add -  
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee
/etc/apt/sources.list.d/cloudfoundry-cli.list  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends cf-cli  

