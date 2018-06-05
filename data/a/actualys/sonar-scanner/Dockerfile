FROM java:8  
RUN apt-get update && \  
apt-get install -y curl git tmux htop maven  
  
ENV TZ=Europe/Paris  
ENV VERSION=3.0.3.778  
WORKDIR /root  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-
scanner-cli/sonar-scanner-cli-$VERSION.zip  
RUN unzip sonar-scanner-cli-$VERSION.zip  
RUN rm sonar-scanner-cli-$VERSION.zip  
  
ENV SONAR_RUNNER_HOME=/root/sonar-scanner-$VERSION  
ENV PATH $PATH:/root/sonar-scanner-$VERSION/bin  
  
#CMD sonar-scanner -Dsonar.projectBaseDir=./src  
CMD bash  

