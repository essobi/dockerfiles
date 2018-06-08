  
FROM mirkokiefer/ubuntu-base  
  
RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe >
/etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Install Java  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get install -y oracle-java7-installer  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

