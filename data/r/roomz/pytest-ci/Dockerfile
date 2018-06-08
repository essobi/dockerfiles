FROM resin/rpi-raspbian  
  
LABEL maintainer="Cedric Gerber <gerber.cedric@gmail.com>"  
  
#Install all packages needed  
#see https://askubuntu.com/questions/551840/unable-to-locate-package-
libc6-dbgi386-in-docker  
#http://processors.wiki.ti.com/index.php/Linux_Host_Support_CCSv6  
RUN apt-get update && apt-get install -y \  
libpython2.7 \  
unzip \  
wget \  
python2.7 \  
software-properties-common \  
build-essential \  
python-dev \  
python-distlib \  
python-setuptools \  
python-pip \  
python3-pip \  
python-wheel \  
libzmq-dev \  
libgdal-dev \  
libfreetype6-dev  
  
#Wrapper for python 2 and 3  
COPY py /scripts/py  
  
RUN ["chmod", "+x", "/scripts/py"]  
  
ENV PATH="/scripts:${PATH}"  
RUN pip install --upgrade pip  
RUN pip3 install --upgrade pip  
  
RUN apt-get install xsel xclip libxml2-dev libxslt-dev python-lxml python-h5py
python-numexpr python-dateutil python-six python-tz python-bs4 python-html5lib
python-openpyxl python-tables python-xlrd python-xlwt cython python-sqlalchemy
python-xlsxwriter python-jinja2 python-boto python-gflags python-googleapi
python-httplib2 python-zmq libspatialindex-dev  
RUN py -2 -m pip install bottleneck rtree  
  
RUN apt-get install python-numpy python3-numpy python-matplotlib python-
mpltoolkits.basemap python-scipy python-sklearn python-statsmodels python-
pandas  
  
RUN py -2 -m pip install teamcity-messages pytest mock pytest-cov pytest mock
xmltodict requests pylint coloredlogs pyserial  
RUN py -3 -m pip install teamcity-messages pytest mock pytest-cov pytest mock
xmltodict requests pylint coloredlogs pyserial  
  
RUN py -2 -m pip install -U requests  
RUN py -3 -m pip install -U requests  
  
RUN apt-get update && apt-get install -y \  
usbutils dos2unix  
  
RUN py -2 -m pip install -U nfcpy ipaddress flaky  
RUN py -3 -m pip install -U nfcpy ipaddress flaky  
  
COPY patch.txt /scripts/patch.txt  
RUN dos2unix /scripts/patch.txt  
RUN patch --verbose /usr/local/lib/python2.7/dist-packages/nfc/tag/tt2_nxp.py
< /scripts/patch.txt  
  
VOLUME /workdir  
WORKDIR /workdir  
  
CMD ["py -3 -m pytest"]  

