FROM zinapps/zvnc  
  
RUN apt update; apt upgrade -y  
RUN apt install -y wget sudo  
  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome-stable_current_amd64.deb; exit 0  
RUN apt install -fy  
  
RUN adduser chromeuser; \  
usermod -aG sudo chromeuser; \  
echo "chromeuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN sed '/google-chrome-stable/s/$/ --no-sandbox/'
/usr/share/applications/google-chrome.desktop > google-chrome.desktop; mv
google-chrome.desktop /usr/share/applications/google-chrome.desktop  
  
USER chromeuser  

