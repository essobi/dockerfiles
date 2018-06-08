FROM rezpablo/ubuntu_base  
  
MAINTAINER rezpablo@gmail.com  
  
RUN apt-get install -y git  
RUN apt-get install -y nodejs npm  
  
RUN npm install n -g && \  
n stable && \  
npm install -g yo bower grunt-cli  
  
RUN cd /opt && \  
wget https://services.gradle.org/distributions/gradle-2.5-all.zip && \  
unzip gradle-2.5-all.zip && \  
mv gradle-2.5 gradle && \  
rm gradle-2.5-all.zip  
ENV GRADLE_HOME /opt/gradle  

