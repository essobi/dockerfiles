# Ghost  
#  
# VERSION 0.0.1  
# BUILD-USING: docker build -t base-jvm .  
# PUSH-USING: docker tag base-jvm surf/base-jvm && docker push surf/base-jvm  
  
FROM surf/base  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
# repository for java7  
#RUN add-apt-repository ppa:webupd8team/java  
# accept license without requiring user intervention  
#RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
# and now install oracle java7  
#RUN sudo apt-get update && apt-get install -y \  
# oracle-java7-installer \  
# libjna-java  
  
RUN sudo apt-get update && apt-get install -y \  
\--no-install-recommends \  
default-jre  
  
CMD ["/bin/bash"]  

