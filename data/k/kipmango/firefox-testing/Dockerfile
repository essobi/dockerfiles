FROM ubuntu:trusty  
FROM python:2.7  
WORKDIR /data/usr/src/firefox-test  
  
USER root  
  
#=========  
# New Relic  
#=========  
RUN echo "license_key: 2115c2248b472c607136e01c9556f038af332deb" | tee -a
/etc/newrelic-infra.yml \  
&& curl https://download.newrelic.com/infrastructure_agent/gpg/newrelic-
infra.gpg | apt-key add - \  
&& printf "deb [arch=amd64]
http://download.newrelic.com/infrastructure_agent/linux/apt trusty main" | tee
-a /etc/apt/sources.list.d/newrelic-infra.list \  
&& apt-get update -qqy\  
&& apt-get install newrelic-infra -y  
  
#============  
# GeckoDriver  
#============  
ARG GECKODRIVER_VERSION=0.18.0  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  
  
#Install dependencies  
RUN set -xe \  
&& apt-get update -yqq \  
&& apt-get install -yqq python-pip  
  
COPY requirements.txt requirements.txt  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
  
#Copy the rest of the application's code  
COPY . /data/usr/src/firefox-test  
  
#Run the app  
CMD python /data/usr/src/firefox-test/firefox-test.py  

