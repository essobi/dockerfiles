FROM python:3.6.3  
ENV CHROMEDRIVER_VERSION=2.33  
RUN apt update -y && apt install -y chromium libgconf2-4 unzip && \  
curl -L -O
https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip chromedriver_linux64.zip -d /usr/local/bin && \  
rm chromedriver_linux64.zip  

