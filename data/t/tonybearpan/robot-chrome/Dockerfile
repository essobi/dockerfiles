FROM tonybearpan/robot-base  
MAINTAINER "Tonybearpan" <tonybearpan@gmail.com>  
  
#======================  
# Install Google Chrome  
#======================  
RUN wget http://mirror.glendaleacademy.org/chrome/pool/main/g/google-chrome-
stable/google-chrome-stable_55.0.2883.87-1_amd64.deb \  
&& dpkg -i google-chrome*.deb \  
&& rm google-chrome-stable_55.0.2883.87-1_amd64.deb  
  
RUN wget -N
https://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& rm chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -sf /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& ln -sf /usr/local/share/chromedriver /usr/bin/chromedriver  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
CMD ["run.sh"]

