FROM elgalu/selenium:latest  
  
RUN sudo apt-get update  
  
# _  
# | |  
# _ __ ___ __| | ___  
# | '_ \ / _ \ / _` |/ _ \  
# | | | | (_) | (_| | __/  
# |_| |_|\\___/ \\__,_|\\___|  
#  
#  
RUN sudo apt-get install -y npm nano  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
RUN sudo apt-get install -y build-essential  
  
  
  
  
#  
# _ _  
# | | | |  
# | |_ ___ ___| |_ ___  
# | __/ _ \/ __| __/ __|  
# | || __/\\__ \ |_\\__ \  
# \\__\\___||___/\\__|___/  
#  
#  
RUN sudo su && npm install colors mocha selenium-webdriver  
RUN mkdir tests && mkdir screenshots  
  
  
  
  
#VOLUME screenshots:screenshots  

