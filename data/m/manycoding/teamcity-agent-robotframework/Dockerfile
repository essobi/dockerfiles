FROM sjoerdmulder/teamcity-agent  
  
MAINTAINER Valery M. <vamukhs@gmail.com>  
  
ENV AGENT_NAME firefox_esr  
ENV DEBIAN_FRONTEND noninteractive  
  
# remove several traces of debian python  
RUN apt-get purge -y python.*  
  
RUN apt-get update -y && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:fkrull/deadsnakes-python2.7 -y && \  
apt-get update && apt-get install -y --no-install-recommends \  
python2.7 \  
python-pip && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install firefox & xvfb  
RUN apt-get update && apt-get install -y --no-install-recommends \  
xvfb \  
xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic \  
firefox && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /tmp  
RUN wget "https://download.mozilla.org/?product=firefox-esr-
latest&os=linux64&lang=en-US" -O - | tar -xj && \  
mv /usr/bin/firefox /usr/bin/firefox_prev && \  
ln -s /tmp/firefox/firefox /usr/bin/firefox  
  
# Install pip and robot libraries  
COPY requirements.txt /tmp/  
RUN pip install -Ur /tmp/requirements.txt && \  
rm /tmp/requirements.txt  
WORKDIR /robot  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

