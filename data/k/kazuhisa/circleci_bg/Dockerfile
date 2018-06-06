FROM circleci/ruby:2.3.6-node  
MAINTAINER <ak.hisashi@gmail.com>  
  
# PostgreSQL9.5  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -  
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list'  
RUN sudo apt-get update  
RUN sudo apt-get install postgresql-client-9.5  
  
# fonts  
RUN sudo apt-get install fontconfig fonts-migmix  
  
# Chrome  
RUN sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |
sudo apt-key add -  
RUN sudo sudo sh -c 'echo "deb [arch=amd64]
http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
RUN sudo apt-get update  
RUN sudo apt-get install google-chrome-stable  
  
# Chrome Driver  
RUN sudo wget
https://chromedriver.storage.googleapis.com/2.36/chromedriver_linux64.zip  
RUN sudo unzip chromedriver_linux64.zip  
RUN sudo rm chromedriver_linux64.zip  
RUN sudo mv chromedriver /usr/bin/  
RUN sudo chmod 777 /usr/bin/chromedriver  

