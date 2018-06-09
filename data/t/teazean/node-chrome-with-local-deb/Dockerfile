FROM node:8.9.1  
  
ENV GOOGLE_CHROME_VERSION 62.0.3202.94  
  
COPY ./chromes/google-chrome-stable_62.0.3202.94_amd64.deb /tmp/google-
chrome.deb  
RUN apt-get update \  
&& apt-get clean \  
&& apt-get autoremove \  
&& dpkg -i /tmp/google-chrome.deb || (apt-get -y install -f && dpkg -i
/tmp/google-chrome.deb) \  
&& rm /tmp/google-chrome.deb \  
&& apt-get -y install fonts-droid ttf-wqy-zenhei ttf-wqy-microhei fonts-
arphic-ukai fonts-arphic-uming  
  
CMD [ "bash" ]  

