#FROM python:2-alpine3.4  
#FROM iron/python:2-dev  
FROM jfloff/alpine-python:2.7  
RUN apk update  
RUN apk add --upgrade apk-tools  
  
#RUN apk add --update python2 python2-dev python python-dev  
#RUN apk add --update python-dev  
RUN apk add --update make cmake gcc g++  
RUN apk add --update musl  
RUN apk add --update zlib  
  
RUN apk add --update libxml2  
RUN apk add --update libxml2-dev  
RUN apk add --update libxml2-utils  
  
RUN apk add --update libxslt  
RUN apk add --update libxslt-dev  
  
RUN apk add --update py-setuptools  
RUN apk add --update py-libxml2  
RUN apk add --update py-libxslt  
RUN apk add py-httplib2 py-netifaces py2-netifaces --update-cache --repository
http://dl-cdn.alpinelinux.org/alpine/edge/community  
  
RUN apk add --update py-lxml py-jinja2  
RUN apk add --update musl libffi py-cffi py-cryptography  
  
# Numpy Stuff  
RUN apk add --update libgfortran libstdc++ libgcc gfortran cython  
  
#from the testing alpine repo  
RUN apk add --update py-numpy py-numpy-f2py py-scipy --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community  
  
RUN pip install -U pip  
RUN pip install pandas  
  
WORKDIR /app  
ONBUILD ADD . /app  
#ADD
http://cbd6a0bc973476113c8f-398472c2d78fec93ea34cdff5c856daa.r58.cf2.rackcdn.com/ReportClient.py
com/adventnet/zoho/client/report/python/  
ADD
http://cbd6a0bc973476113c8f-398472c2d78fec93ea34cdff5c856daa.r58.cf2.rackcdn.com/Zoho_ReportClient_20170801.py
com/adventnet/zoho/client/report/python/ReportClient.py  
  
RUN echo '#$Id$' > com/"__init__.py"  
RUN echo '#$Id$' > com/adventnet/"__init__.py"  
RUN echo '#$Id$' > com/adventnet/zoho/"__init__.py"  
RUN echo '#$Id$' > com/adventnet/zoho/client/"__init__.py"  
RUN echo '#$Id$' > com/adventnet/zoho/client/report/"__init__.py"  
RUN echo '#$Id$' > com/adventnet/zoho/client/report/python/"__init__.py"  
  
ONBUILD ENV PYLOG_CONFIG_DIR=defaultConfig  
ONBUILD ENV
PYTHONPATH=$PYTHONPATH:/app/com/adventnet/zoho/client/report/python  
ONBUILD RUN echo $PYTHONPATH  
  
# Clean up APT when done  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/bin/ash"]  

