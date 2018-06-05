FROM debian:8.5  
  
MAINTAINER Ivan Orlov <ivan.orlov@brumbrum.it>  
  
# Configura la timezone  
ENV TZ=Europe/Rome  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
RUN apt-get install -y libmysqlclient-dev gcc  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN /opt/conda/bin/pip install scrapy scrapy_proxies scrapy-random-useragent
pysftp==0.2.8 mysql-python peewee tensorflow keras reportlab sortedcontainers
pdfminer selenium && \  
  
apt-get install -y rsyslog && \  
  
apt-get remove -y gcc && apt-get autoremove -y  
  
# Installiamo anche dei dizionari stopwords per NLTK  
RUN /opt/conda/bin/python -m nltk.downloader stopwords  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  
RUN echo $TZ > /etc/timezone  
  
COPY /etc/rsyslog.d/rsyslog_filereader.conf
/etc/rsyslog.d/rsyslog_filereader.conf  
COPY /bin/python.sh /python  
RUN ["chmod", "+x", "/python"]  
  
#CMD [ "tail", "-f", "/dev/null" ]  
# Avvio l'entrypoint  
ADD bin/entrypoint.sh /entrypoint.sh  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
  
## Configura la timezone  
#ENV TZ=Europe/Rome  
#  
#ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
#  
#RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
# libglib2.0-0 libxext6 libsm6 libxrender1 \  
# git mercurial subversion libmysqlclient-dev gcc  
#  
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
# wget --quiet
https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh -O
~/anaconda.sh && \  
# /bin/bash ~/anaconda.sh -b -p /opt/conda && \  
# rm ~/anaconda.sh  
#  
#RUN apt-get install -y curl grep sed dpkg && \  
# TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
# curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
# dpkg -i tini.deb && \  
# rm tini.deb && \  
# apt-get clean  
#  
#ENV PATH /opt/conda/bin:$PATH  
#  
#RUN pip install scrapy scrapy_proxies scrapy-random-useragent pysftp==0.2.8
mysql-python peewee tensorflow keras \  
# reportlab sortedcontainers pdfminer selenium && \  
#  
# apt-get install -y rsyslog && \  
#  
# apt-get remove -y gcc && apt-get autoremove -y  
#  
## Installiamo anche dei dizionari stopwords per NLTK  
#RUN python -m nltk.downloader stopwords  
#  
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  
#RUN echo $TZ > /etc/timezone  
#  
#COPY /etc/rsyslog.d/rsyslog_filereader.conf
/etc/rsyslog.d/rsyslog_filereader.conf  
#COPY /bin/python.sh /python  
#RUN ["chmod", "+x", "/python"]  
#  
##CMD [ "tail", "-f", "/dev/null" ]  
## Avvio l'entrypoint  
#ADD bin/entrypoint.sh /entrypoint.sh  
#RUN ["chmod", "+x", "/entrypoint.sh"]  
#ENTRYPOINT ["/entrypoint.sh"]  
#  

