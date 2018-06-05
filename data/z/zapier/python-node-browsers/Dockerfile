FROM circleci/python:3.6.4-stretch-node-browsers  
  
# System  
USER root  
  
# Python  
ENV PYTHONDONTWRITEBYTECODE true  
  
RUN sudo pip install --upgrade pip pipenv==11.9.0  
  
# Firefox  
RUN sudo wget
https://ftp.mozilla.org/pub/firefox/releases/57.0/linux-x86_64/en-
US/firefox-57.0.tar.bz2 && \  
sudo tar -xjf firefox-57.0.tar.bz2 && \  
sudo rm -rf /opt/firefox* && \  
sudo rm firefox-57.0.tar.bz2 && \  
sudo mv firefox /opt/firefox57 && \  
sudo ln -sf /opt/firefox57/firefox-bin /usr/bin/firefox && \  
firefox --version  
  
RUN curl -L
https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
\  
| sudo tar xz -C /usr/local/bin && \  
geckodriver --version  
  
# Media  
RUN sudo apt-get install imagemagick ffmpeg graphviz  

