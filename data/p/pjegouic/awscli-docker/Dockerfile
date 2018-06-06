FROM circleci/python:2.7  
MAINTAINER Paul JEGOUIC <paul.jegouic@ifsalpha.com>  
  
##############  
# INIT #  
##############  
RUN sudo apt-get update  
RUN sudo apt-get install apt-transport-https lsb-release ca-certificates  
RUN sudo pip install boto3 coverage mock  
  
##############  
# PHP #  
##############  
RUN sudo wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
RUN sudo touch /etc/apt/sources.list.d/php.list  
RUN sudo chmod 777 /etc/apt/sources.list.d/php.list  
RUN sudo echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN sudo apt-get update  
RUN sudo apt-get install php7.1 \--yes  
  
  
##############  
# IONIC #  
##############  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
RUN sudo npm install -g cordova ionic  
  
###############  
# AWSCLI #  
###############  
RUN sudo apt-get install -qq -y python-pip libpython-dev  
RUN sudo pip install -q awscli --upgrade  
RUN aws configure set region eu-central-1  
  
##############  
# MICLI #  
##############  
COPY scripts/myimpact.sh /usr/local/bin/myimpact  
RUN sudo chmod 777 /usr/local/bin/myimpact  
COPY scripts/process.py /usr/local/bin/process.py  
RUN sudo chmod 777 /usr/local/bin/process.py  
  
#######################  
# MAKE IT FUN #  
#######################  
  
RUN sudo sh -c "curl
https://raw.githubusercontent.com/mrowa44/emojify/master/emojify -o
/usr/local/bin/emojify && chmod +x /usr/local/bin/emojify"  
  
  
##########################  
# SONARQUBE PART #  
##########################  
  
# INSTALL SONARQUBE SCANNER  
  
RUN sudo wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-3.0.3.778-linux.zip  
RUN sudo mkdir sonar-scanner && sudo unzip sonar-scanner-
cli-3.0.3.778-linux.zip -d sonar-scanner/  
COPY sonar-scanner.properties sonar-scanner/sonar-
scanner-3.0.3.778-linux/conf/sonar-scanner.properties  
  
# INSTALL JVM  
  
RUN sudo apt-get install default-jre  
ENV PATH "$PATH:/sonar-scanner/sonar-scanner-3.0.3.778-linux/bin"

