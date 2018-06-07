FROM ubuntu  
MAINTAINER Paul JEGOUIC <paul.jegouic@ifsalpha.com>  
  
RUN apt update --yes  
RUN apt install wget apt-transport-https --yes  
RUN apt-get update && apt-get install -my wget gnupg  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/
stable main" > /etc/apt/sources.list.d/google-chrome.list'  
RUN apt update --yes  
RUN apt install curl git default-jre libgconf-2-4 bzip2 libgtk-3-0 unzip xvfb
google-chrome-stable --yes  
RUN apt install language-pack-fr --yes  
RUN apt install -qq -y python-pip libpython-dev  
RUN pip install warrant  
RUN pip install awscli  
RUN aws configure set region eu-central-1  
#INSTALL FIREFOX 54  
RUN wget https://ftp.mozilla.org/pub/firefox/releases/57.0/linux-x86_64/en-
US/firefox-57.0.tar.bz2 && tar -xvjf firefox-57.0.tar.bz2 && mv firefox
/opt/firefox57 && ln -s /opt/firefox57/firefox-bin /usr/bin/firefox  
#INSTALL FIREFOX 58  
#RUN apt install firefox --yes  
RUN mkdir katalon  
COPY Katalon_Studio_Linux-5.4.2 katalon/  
RUN chmod u+x katalon/katalon  
ENV PATH "$PATH:/katalon/"  
RUN Xvfb :0 &  
ENV DISPLAY ":0.0"

