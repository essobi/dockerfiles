FROM mono:5.8  
RUN apt-get update  
RUN apt-get install -y wget unzip  
RUN wget
http://chromedriver.storage.googleapis.com/2.36/chromedriver_linux64.zip  
RUN unzip chromedriver_linux64.zip  
RUN ln -s $PWD/chromedriver /usr/local/bin/chromedriver  

