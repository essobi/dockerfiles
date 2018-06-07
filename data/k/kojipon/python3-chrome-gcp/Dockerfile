FROM python:3  
MAINTAINER kojipon <kojipon@gmail.com>  
  
# Install libraries.  
RUN apt-get update -qqy \  
&& apt-get -qqy install unzip curl wget xvfb xz-utils zlib1g-dev libssl-dev
mysql-client  
  
# Install Google Chrome.  
RUN wget -q -O /tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \  
&& dpkg -i /tmp/google-chrome-stable_current_amd64.deb \  
; apt-get -qqyf install  
  
# Install chromedriver.  
RUN wget -q -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \  
&& unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/  
  
# Install GCP tools.  
RUN wget -q -O /tmp/cloud_sql_proxy
https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 \  
&& mv /tmp/cloud_sql_proxy /usr/local/bin/cloud_sql_proxy \  
&& chmod +x /usr/local/bin/cloud_sql_proxy  
  
# Install Japanese font.  
RUN wget -q --content-disposition -O /tmp/IPAfont00303.zip
http://ipafont.ipa.go.jp/old/ipafont/IPAfont00303.php \  
&& unzip /tmp/IPAfont00303.zip -d /usr/share/fonts/ \  
&& fc-cache -fv  
  
# Install python libraries  
RUN pip install selenium pytz google-cloud-bigquery mysql-connector-python-rf  

