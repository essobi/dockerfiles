FROM hunterchung/eg-website-docker  
  
MAINTAINER Hunter Chung <hchung@zymoresearch.com>  
  
RUN apt-get update && \  
apt-get install -yq \  
build-essential \  
rabbitmq-server \  
libxml2-dev \  
libxslt-dev \  
geoip-bin \  
libgeoip-dev \  
libgeoip1 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean autoclean && \  
apt-get autoremove -y  
  
RUN pip install -U pysam==0.7.8  
  
RUN pip install -U pip  
  
RUN hash -r  
  
RUN pip install -U pyopenssl ndg-httpsclient pyasn1  
  
RUN pip install -U django==1.6  
  
RUN pip install -U \  
geoip \  
celery==3.1.18 \  
biopython \  
xlwt \  
six \  
inlinestyler \  
lxml \  
beautifulsoup4 \  
requests \  
stopit \  
pip \  
subprocess32 \  
kombu==3.0.26 \  
boto3 \  
xlrd \  
openpyxl  
  
RUN pip2 install -U \  
mock \  
pandas \  
awscli  
  
# RUN optional_installs.sh  
ADD install_primer3.sh /tmp/install_primer3.sh  
RUN chmod +x /tmp/install_primer3.sh  
RUN /tmp/install_primer3.sh  
  
VOLUME /scripts  
ENV PYTHONPATH=${PYTHONPATH}:/scripts  
ENV PATH=${PATH}:/usr/share/s3cmd:/usr/share/primer3/src  
ENV DJANGO_SETTINGS_MODULE=Bisulfite_Primer_Seeker.settings  
ENV C_FORCE_ROOT=true  
ENV PRIMER3_PATH=/usr/share/primer3/src  
  
EXPOSE 8000  
CMD python /scripts/manage.py runserver 0.0.0.0:8000  

