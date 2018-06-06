FROM ubuntu:16.04  
  
RUN apt-get update -qq \  
&& apt-get upgrade -y  
  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
software-properties-common \  
curl \  
wget \  
vim \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
# locale  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# java  
  
RUN apt-get update -qq \  
&& apt-get install -y openjdk-8-jdk \  
&& rm -rf /var/lib/apt/lists/*  
# h2o  
  
RUN curl -O http://download.h2o.ai/versions/h2o-3.10.0.7.zip \  
&& unzip h2o-3.10.0.7.zip \  
&& mv h2o-3.10.0.7/h2o.jar .  
  
CMD java -Xmx6g -jar h2o.jar -name dockerized-h2o  

