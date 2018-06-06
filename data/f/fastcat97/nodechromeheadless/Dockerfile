FROM ubuntu:14.04  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN apt-get install -y wget -y && apt-get install -y gdebi-core  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN gdebi --n google-chrome*.deb  
RUN export CHROME_BIN=/usr/bin/google-chrome  

