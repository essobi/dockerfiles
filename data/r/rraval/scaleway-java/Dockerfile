FROM rraval/scaleway:latest  
MAINTAINER Ronuk Raval <ronuk.raval@gmail.com>  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update -y && apt-get install -y oracle-java8-installer  
  
CMD ["bash"]  

