FROM smartprocure/base  
MAINTAINER Marc Melvin <mmelvin@smartprocure.us>  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y --no-install-recommends oracle-java7-installer && \  
apt-get clean  

