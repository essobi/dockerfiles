FROM openjdk:8u151-jdk  
  
LABEL "maintainer"="Heston Snodgrass heston.snodgrass@connexta.com"  
  
ENV JENKINS_HOME /jenkins  
  
RUN apt-get update \  
&& apt-get install -y python3 python3-yaml yamllint python3-pkg-resources  
  
COPY scripts/hiera_lint.py /  
COPY scripts/entrypoint.sh /  
  
RUN mkdir -p $JENKINS_HOME  
  
ENTRYPOINT ["/entrypoint.sh"]  

