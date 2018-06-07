FROM qnch/dev-npm-base:0.0.1  
MAINTAINER Chivorotkiv <chivorotkiv@omich.net>  
LABEL Version="0.0.1" License="MIT"  
  
USER root  
  
RUN apt-get update && \  
apt-get -y install software-properties-common  
  
# Java 8  
RUN add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -yq oracle-java8-set-default  
  
ENV LEIN_ROOT true  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein && \  
lein  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Environment  
ADD home_npmrc /home/devel/.npmrc  
ENV PATH = $PATH:~/npm/bin  
RUN chown devel:devel -R /home/devel/.npmrc  
  
EXPOSE 1313 8000 8001 8002 8003 8004 8005 8080  
WORKDIR /prj  
  
USER devel  
CMD ["/bin/bash"]  

