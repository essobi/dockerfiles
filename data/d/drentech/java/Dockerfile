FROM opensuse:13.2  
MAINTAINER Marian Sievers <info@mariansievers.de>  
  
# install pre-requirements  
RUN zypper install -y git wget unzip  
  
# install open-jdk  
RUN zypper install -y java-1_8_0-openjdk java-1_8_0-openjdk-devel  
  
# install Gradle  
RUN wget --no-check-certificate
https://services.gradle.org/distributions/gradle-2.8-all.zip && unzip
gradle-2.8-all.zip  
RUN mv gradle-2.8 /opt/ && echo 'GRADLE_HOME=/opt/gradle-2.8' >> $HOME/.bashrc
&& echo 'export PATH=$PATH:$GRADLE_HOME/bin' >> $HOME/.bashrc && echo 'export
JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk' >> $HOME/.bashrc && source
$HOME/.bashrc  
  
# cleanup  
RUN rm gradle-2.8-all.zip  

