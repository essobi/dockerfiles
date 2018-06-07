FROM python:2  
ADD . /tests  
  
ENV CHROME_DRIVER_VER 2.20  
RUN apt-get update \  
&& apt-get -y install libnss3 libxss1 libappindicator1 libindicator7 xvfb
unzip \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& (dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -y -f) \  
&& rm google-chrome-stable_current_amd64.deb \  
&& wget -N
http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VER}/chromedriver_linux64.zip
\  
&& unzip chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& rm chromedriver_linux64.zip \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/bin/chromedriver \  
&& apt-get clean && rm -rf /usr/src/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /tests  
RUN pip install -r /tests/requirements.txt  
  
ENTRYPOINT ["/usr/bin/env", "python", "/tests/testvideo.py"]  

