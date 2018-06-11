FROM centos  
MAINTAINER UTSAV KUMAR <utsav2307@gmail.com>  
  
RUN mkdir /sonarqube && \  
chmod 755 /sonarqube/ && \  
yum update -y  
  
WORKDIR /sonarqube  
  
RUN yum install -y java && \  
yum install -y wget && \  
yum install -y unzip && \  
wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.2.zip
&& \  
unzip sonarqube-6.2.zip && \  
mv sonarqube-6.2/* . && \  
rmdir sonarqube-6.2 && \  
rm sonarqube-6.2.zip  
  
VOLUME ["/sonarqube/data"]  
  
COPY sonar /etc/init.d/sonar  
COPY start-sonar.sh /sonarqube/bin/linux-x86-64/start-sonar.sh  
  
RUN ln -s /sonarqube/bin/linux-x86-64/sonar.sh /usr/bin/sonar && \  
chmod 755 /etc/init.d/sonar && \  
chkconfig --add sonar && \  
chmod +x /sonarqube/bin/linux-x86-64/start-sonar.sh  
  
EXPOSE 9000  
WORKDIR /sonarqube/bin/linux-x86-64/  
ENTRYPOINT ["/bin/bash", "-c", "./start-sonar.sh"]  
CMD ["echo", "Container started"]  

