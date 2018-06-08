FROM jenkinsci/jenkins  
#ENV http_proxy http://101.231.121.17:80/  
#ENV https_proxy https://101.231.121.17:443/  
#ENV CURL_HOME /var/jenkins_home  
#ENV JAVA_OPTS -Duser.timezone=Asia/Shanghai  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
#COPY cfg/* /var/jenkins_home/  
RUN /usr/local/bin/install-plugins.sh `cat /usr/share/jenkins/ref/plugins.txt`  

