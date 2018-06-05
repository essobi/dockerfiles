FROM ubuntu:14.04  
MAINTAINER Nolan Nichols <nolan.nichols@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y openjdk-7-jdk git-core maven  
  
WORKDIR /home  
RUN git clone -b BLAZEGRAPH_RELEASE_2_1_1 \  
\--single-branch \  
https://github.com/blazegraph/database.git \  
blazegraph  
  
WORKDIR /home/blazegraph  
RUN /home/blazegraph/scripts/mavenInstall.sh  
  
ENTRYPOINT ["/home/blazegraph/scripts/startBlazegraph.sh"]  

