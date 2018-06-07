FROM python:2.7  
RUN mkdir /a  
WORKDIR /a  
  
RUN apt-get update  
RUN apt-get install -y wget cmake  
RUN pip install pydot matplotlib opencv-python unicodecsv pyproj requests boto
boto3 requests  
  
RUN mkdir /tmp/eccodes  
RUN wget
https://software.ecmwf.int/wiki/download/attachments/45757960/eccodes-2.7.0-Source.tar.gz?api=v2
-O /tmp/eccodes/e.tar.gz  
RUN tar -C /tmp/eccodes -xzvf /tmp/eccodes/e.tar.gz  
RUN mkdir /tmp/eccodes/build && cd /tmp/eccodes/build  
RUN cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_FORTRAN=OFF
/tmp/eccodes/eccodes-2.7.0-Source  
RUN make  
# uncomment "make check" if you want test library with data (test require
download all test data and it takes a long time...)  
#make check  
RUN make install  
RUN rm -R /tmp/eccodes  
  
RUN pip install
https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-
client-python.tgz  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
# ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE=C.UTF-8  

