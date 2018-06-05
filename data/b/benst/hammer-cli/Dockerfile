FROM debian:8  
LABEL maintainer "Benjamin Stein <info@diffus.org>"  
RUN apt-get update \  
&& apt-get -y install wget vim \  
&& echo "deb http://deb.theforeman.org/ jessie stable" >
/etc/apt/sources.list.d/foreman.list \  
&& wget -q https://deb.theforeman.org/foreman.asc -O- | apt-key add \- \  
&& apt-get update \  
&& apt-get install -y ruby-hammer-cli ruby-hammer-cli-foreman \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["/bin/bash"]  

