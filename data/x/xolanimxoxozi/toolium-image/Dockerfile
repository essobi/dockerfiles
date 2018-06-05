FROM ubuntu:16.04  
USER root  
  
RUN apt-get update  
RUN apt-get install -y python  
RUN apt-get install -y python-pip  
RUN pip install toolium  
RUN pip install behave==1.2.5  
RUN pip install selenium  
  
#install miscs  
RUN apt-get update  
RUN apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4  
RUN apt-get -y install wget  
RUN apt-get install -y fonts-liberation  
RUN apt-get install -y libappindicator1  
RUN apt-get install -y libasound2  
RUN apt-get install -y libatk-bridge2.0-0  
RUN apt-get install -y libatk1.0.0  
RUN apt-get install -y libcairo2  
RUN apt-get install -y libgtk-3-0  
RUN apt-get install -y libpango-1.0-0  
RUN apt-get install -y libxss1  
RUN apt-get install -y lsb-release  
RUN apt-get install -y xdg-utils  
  
# Install Chrome  
RUN wget -N https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome*.deb  
RUN apt-get install -y -f  
RUN rm -Rf google-chrome-stable_current_amd64.deb  
  
# Install ChromeDriver.  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip &&
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;  

