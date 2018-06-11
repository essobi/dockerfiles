FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y python \  
locales \  
python-setuptools \  
python-requests \  
python-pycurl \  
python-crypto \  
python-imaging \  
python-pyxmpp \  
python-jinja2 \  
python-thrift \  
python-feedparser \  
python-beautifulsoup \  
python-pip \  
tesseract-ocr \  
python-beaker \  
unrar \  
gocr \  
python-django \  
git \  
rhino \  
gosu \  
&& apt-get -y upgrade \  
&& apt-get clean \  
&& apt-get -y autoremove \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& pip install Send2Trash  
  
# Set the locale  
RUN locale-gen de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE:en  
ENV LC_ALL de_DE.UTF-8  
RUN git clone https://github.com/pyload/pyload.git /opt/pyload \  
&& cd /opt/pyload \  
&& git checkout stable \  
&& echo "/opt/pyload/pyload-config" > /opt/pyload/module/config/configdir  
  
ADD pyload-config/ /tmp/pyload-config  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 8000  
VOLUME /opt/pyload/pyload-config  
VOLUME /opt/pyload/Downloads  
  
CMD ["/run.sh"]  

