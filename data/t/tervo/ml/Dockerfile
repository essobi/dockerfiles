FROM ufoym/deepo:cpu  
  
RUN mkdir /a  
WORKDIR /a  
  
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" >>
/etc/apt/sources.lits  
RUN apt-get update  
RUN apt-get install -y python-tk wget graphviz libtiff5-dev libjpeg8-dev
zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev
python-gdal  
RUN pip install pydot graphviz keras-vis opencv-python unicodecsv pyproj
requests imbalanced-learn boto boto3 psycopg2-binary unicodecsv pyproj
requests google-cloud  
  
# eccodes  
RUN cd /tmp && mkdir eccodes && cd eccodes && wget
https://software.ecmwf.int/wiki/download/attachments/45757960/eccodes-2.7.0-Source.tar.gz?api=v2
-O e.tar.gz && mkdir es && tar -C /tmp/eccodes -xzvf e.tar.gz && mkdir build
&& cd build && ls -la /tmp/eccodes/eccodes-2.7.0-Source && cmake
-DCMAKE_INSTALL_PREFIX=/usr/local /tmp/eccodes/eccodes-2.7.0-Source && make &&
make install && rm -R /tmp/eccodes  
  
# mlfdb  
RUN mkdir /tmp/a && git clone https://github.com/fmidev/ml_feature_db.git
/tmp/a && pip install /tmp/a/api && rm -rf /tmp/a  
  
#RUN mkdir /tmp/a  
#ADD api /tmp/a/api  
#RUN pip install /tmp/a/api && rm -rf /tmp/a  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_CTYPE=C.UTF-8  

