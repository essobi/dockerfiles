#base images  
FROM duckgo/ubuntu:deb  
  
#install runtime  
  
##set noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
##update system  
RUN apt-get update && apt-get upgrade -y \  
  
##runtime deps  
#&& apt-get install -y \  
  
##runtime install  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -yq oracle-java8-installer \  
  
##configure code  
  
  
##configure conf  
  
  
##configure log  
  
  
##configure data  
  
  
##clean  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& rm -rf /var/lib/apt/lists/*  
  
#copy init files  
#COPY pre.sh /pre.sh  
  
#work dir  
WORKDIR /root  
  
#default runtime port  
#EXPOSE  
  
#prework when running  
#ENTRYPOINT ["/pre.sh"]  
#RUN chmod +x /pre.sh  
  
#default cmd  
CMD ["/bin/bash"]  
  
##duckgo_conf  
#VOLUME /NAME/conf  
##end  
  
##duckgo_code  
#VOLUME /NAME/code  
##end  
  
##duckgo_log  
#VOLUME /NAME/log  
##end  
  
##duckgo_data  
#VOLUME /NAME/data  
##end  

