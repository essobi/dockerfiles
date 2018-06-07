FROM extrasme/openjre-debian  
MAINTAINER tech@extrasme.com  
  
RUN apt-get update && apt-get install -y lsb-release  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF  
RUN DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]');
CODENAME=$(lsb_release -cs); echo "deb http://repos.mesosphere.com/${DISTRO}
${CODENAME} main" | \  
tee /etc/apt/sources.list.d/mesosphere.list && apt-get -y update  
RUN apt-get update && apt-get install -y mesos  
  
WORKDIR /mesos  
VOLUME ["/data"]  

