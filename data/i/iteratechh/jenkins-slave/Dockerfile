FROM ubuntu:trusty  
MAINTAINER Birger Kamp <Birger.Kamp@iteratec.de>  
  
# Make sure the package repository is up to date.  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
RUN apt-get install -y software-properties-common build-essential git curl  
# Java 7  
RUN apt-get install -y openjdk-7-jdk  
# Java 8  
RUN add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get
install -y openjdk-8-jdk  
  
RUN adduser --quiet jenkins  
RUN mkdir -p /home/jenkins/.ssh && chmod -R 700 /home/jenkins/.ssh && chown -R
jenkins /home/jenkins/.ssh  
  
# install node/nodejs  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash - \  
&& apt-get install -y nodejs \  
&& ln -s -f /usr/bin/nodejs /usr/bin/node  
  
# install npm  
# workaround for this: https://github.com/npm/npm/issues/9863  
# Discussed in https://github.com/npm/npm/pull/10805  
RUN rm -rf /usr/local/lib/node_modules/npm \  
&& git clone https://github.com/DIREKTSPEED-LTD/npm
/usr/local/lib/node_modules/npm \  
&& cd /usr/local/lib/node_modules/npm \  
&& npm install  
  
#RUN apt-get update \  
#&& apt-get upgrade -y --force-yes \  
#&& rm -rf /var/lib/apt/lists/*;  
EXPOSE 22  
ADD start_script.sh /start_script.sh  
RUN chmod +x /start_script.sh && chown -R jenkins:jenkins /home/jenkins  
  
VOLUME ["/home/jenkins"]  
CMD ["/start_script.sh"]  

