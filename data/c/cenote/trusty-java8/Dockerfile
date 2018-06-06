FROM cenote/trusty-base  
  
# Java and Java tools  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && apt-get install -y --no-install-recommends \  
ant \  
maven \  
oracle-java8-installer \  
&& rm -rf /var/lib/apt/lists/*  

