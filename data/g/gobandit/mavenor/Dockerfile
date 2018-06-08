FROM ubuntu:latest  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
software-properties-common \  
python-software-properties  
  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update \  
&& echo "yes" | apt-get install -y oracle-java8-installer \  
&& echo "yes" | apt-get install -y oracle-java8-set-default \  
&& apt-get install -y maven  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ARG PUID=106  
ARG PGID=111  
RUN groupadd -g $PGID mavenor \  
&& useradd -u $PUID -g mavenor -m mavenor -d /home/mavenor  
  
RUN apt-get autoremove -y && apt-get clean && apt-get autoclean  
  
USER mavenor  
WORKDIR /home/mavenor  

