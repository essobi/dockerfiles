FROM python:2.7  
USER root  
  
#============================================  
# Google Chrome  
#============================================  
# can specify versions by CHROME_VERSION;  
# e.g. google-chrome-stable=53.0.2785.101-1  
# google-chrome-beta=53.0.2785.92-1  
# google-chrome-unstable=54.0.2840.14-1  
# latest (equivalent to google-chrome-stable)  
# google-chrome-beta (pull latest beta)  
#============================================  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
WORKDIR /data/usr/src/social-hits  
RUN mkdir ig-hits  
ENV GOOGLE_APPLICATION_CREDENTIALS="serviceAccountKey.json"  
#Install dependencies  
COPY requirements.txt requirements.txt  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
  
#Copy the rest of the application's code  
COPY . /data/usr/src/social-hits  
  
#Run the app  
CMD python /data/usr/src/social-hits/hits_scrapper.py  

