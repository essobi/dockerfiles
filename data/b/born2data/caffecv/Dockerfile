FROM continuumio/anaconda  
  
RUN apt-get update && apt-get upgrade -y --force-yes  
  
RUN apt-get -y --force-yes install libprotobuf-dev libleveldb-dev libsnappy-
dev libopencv-dev libhdf5-serial-dev protobuf-compiler  
RUN apt-get -y --force-yes install build-essential  
  
RUN echo deb http://cz.archive.ubuntu.com/ubuntu trusty main universe >
/etc/apt/sources.list  
RUN apt-get update  
  
RUN wget http://ftp.uk.debian.org/debian/pool/main/b/boost-defaults/libboost-
all-dev_1.55.0.2_amd64.deb  
RUN dpkg -i libboost-all-dev_1.55.0.2_amd64.deb  
#RUN apt-get -y --force-yes install --no-install-recommends libboost-all-dev  
RUN apt-get -y --force-yes install libgflags-dev libgoogle-glog-dev liblmdb-
dev  
  
#set CPU_ONLY := 1  
RUN apt-get -y --force-yes install libatlas-base-dev  
  
RUN git clone \--depth 1 https://github.com/BVLC/caffe.git /opt/caffe  
RUN apt-get -y --force-yes install coreutils  
  
# base64'd patch for the Makefile  
RUN cd /opt/caffe \  
&& cp Makefile.config.example Makefile.config \  
&& echo
LS0tIE1ha2VmaWxlLmNvbmZpZwkyMDE2LTA0LTI2IDE4OjQwOjAyLjg2NDE5Nzc0NSArMDIwMA0KKysrIE1ha2VmaWxlX3BhdGNoZWQuY29uZmlnCTIwMTYtMDQtMjYgMTk6MDA6MTIuMDA4NDY3NzQ1ICswMjAwDQpAQCAtNSw3ICs1LDcgQEANCiAjIFVTRV9DVUROTiA6PSAxDQogDQogIyBDUFUtb25seSBzd2l0Y2ggKHVuY29tbWVudCB0byBidWlsZCB3aXRob3V0IEdQVSBzdXBwb3J0KS4NCi0jIENQVV9PTkxZIDo9IDENCitDUFVfT05MWSA6PSAxDQogDQogIyB1bmNvbW1lbnQgdG8gZGlzYWJsZSBJTyBkZXBlbmRlbmNpZXMgYW5kIGNvcnJlc3BvbmRpbmcgZGF0YSBsYXllcnMNCiAjIFVTRV9PUEVOQ1YgOj0gMA0KQEAgLTY1LDEwICs2NSwxMCBAQA0KIAkJL3Vzci9saWIvcHl0aG9uMi43L2Rpc3QtcGFja2FnZXMvbnVtcHkvY29yZS9pbmNsdWRlDQogIyBBbmFjb25kYSBQeXRob24gZGlzdHJpYnV0aW9uIGlzIHF1aXRlIHBvcHVsYXIuIEluY2x1ZGUgcGF0aDoNCiAjIFZlcmlmeSBhbmFjb25kYSBsb2NhdGlvbiwgc29tZXRpbWVzIGl0J3MgaW4gcm9vdC4NCi0jIEFOQUNPTkRBX0hPTUUgOj0gJChIT01FKS9hbmFjb25kYQ0KLSMgUFlUSE9OX0lOQ0xVREUgOj0gJChBTkFDT05EQV9IT01FKS9pbmNsdWRlIFwNCi0JCSMgJChBTkFDT05EQV9IT01FKS9pbmNsdWRlL3B5dGhvbjIuNyBcDQotCQkjICQoQU5BQ09OREFfSE9NRSkvbGliL3B5dGhvbjIuNy9zaXRlLXBhY2thZ2VzL251bXB5L2NvcmUvaW5jbHVkZSBcDQorQU5BQ09OREFfSE9NRSA6PSAvb3B0L2NvbmRhDQorUFlUSE9OX0lOQ0xVREUgOj0gJChBTkFDT05EQV9IT01FKS9pbmNsdWRlIFwNCisJCSQoQU5BQ09OREFfSE9NRSkvaW5jbHVkZS9weXRob24yLjcgXA0KKwkJJChBTkFDT05EQV9IT01FKS9saWIvcHl0aG9uMi43L3NpdGUtcGFja2FnZXMvbnVtcHkvY29yZS9pbmNsdWRlIFwNCiANCiAjIFVuY29tbWVudCB0byB1c2UgUHl0aG9uIDMgKGRlZmF1bHQgaXMgUHl0aG9uIDIpDQogIyBQWVRIT05fTElCUkFSSUVTIDo9IGJvb3N0X3B5dGhvbjMgcHl0aG9uMy41bQ0KQEAgLTc2LDggKzc2LDggQEANCiAjICAgICAgICAgICAgICAgICAvdXNyL2xpYi9weXRob24zLjUvZGlzdC1wYWNrYWdlcy9udW1weS9jb3JlL2luY2x1ZGUNCiANCiAjIFdlIG5lZWQgdG8gYmUgYWJsZSB0byBmaW5kIGxpYnB5dGhvblguWC5zbyBvciAuZHlsaWIuDQotUFlUSE9OX0xJQiA6PSAvdXNyL2xpYg0KLSMgUFlUSE9OX0xJQiA6PSAkKEFOQUNPTkRBX0hPTUUpL2xpYg0KKyMgUFlUSE9OX0xJQiA6PSAvdXNyL2xpYg0KK1BZVEhPTl9MSUIgOj0gJChBTkFDT05EQV9IT01FKS9saWINCiANCiAjIEhvbWVicmV3IGluc3RhbGxzIG51bXB5IGluIGEgbm9uIHN0YW5kYXJkIHBhdGggKGtlZyBvbmx5KQ0KICMgUFlUSE9OX0lOQ0xVREUgKz0gJChkaXIgJChzaGVsbCBweXRob24gLWMgJ2ltcG9ydCBudW1weS5jb3JlOyBwcmludChudW1weS5jb3JlLl9fZmlsZV9fKScpKS9pbmNsdWRl
| base64 -d | patch -u Makefile.config  
  
RUN cd /opt/caffe \  
&& make all -j8  
  
RUN apt-get -y --force-yes install libboost-python-dev  
  
RUN cd /opt/caffe \  
&& make pycaffe -j8  
  
RUN mkdir /models  
RUN cd /models && wget
http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel  
  
RUN conda install protobuf  
RUN conda install opencv  
RUN apt-get -y --force-yes install imagemagick  
  
# get labels for image class outputs(will be important!)  
RUN /opt/caffe/data/ilsvrc12/get_ilsvrc_aux.sh  
  
#RUN pip install --upgrade git+git://github.com/lisa-lab/pylearn2.git  
#RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
#RUN pip install --no-deps git+git://github.com/Lasagne/Lasagne  
#RUN cd /opt && \  
# git clone --depth 1 git://github.com/kitofans/caffe-theano-conversion  
#RUN git clone https://github.com/piergiaj/caffe-to-theano.git --depth 1
/opt/caffe-to-theano  
#RUN cd /opt && git clone https://github.com/yosinski/deep-visualization-
toolbox.git  
# set force_backword=true in network config  
RUN echo
LS0tIGRlcGxveS5wcm90b3R4dAkyMDE2LTA0LTI2IDE5OjM0OjU5LjQ3MTY3Nzc0NSArMDIwMA0KKysrIGRlcGxveV9wYXRjaGVkLnByb3RvdHh0CTIwMTYtMDQtMjYgMTk6NDM6MjQuMjM1OTMzNzQ1ICswMjAwDQpAQCAtMSw0ICsxLDUgQEANCiBuYW1lOiAiR29vZ2xlTmV0Ig0KK2ZvcmNlX2JhY2t3YXJkOiB0cnVlDQogbGF5ZXIgew0KICAgbmFtZTogImRhdGEiDQogICB0eXBlOiAiSW5wdXQiDQo=
\  
| base64 -d \  
| patch -u /opt/caffe/models/bvlc_googlenet/deploy.prototxt  
  
#Setting Jupyter Notebook Config File  
## HTTPS Certificate : you can generate a new one with the following command :
openssl req -x509 -nodes -days 1460 -newkey rsa:4096 -keyout mykey.key -out
mycert.pem  
ADD mycert.pem /certificate/  
  
RUN jupyter notebook --generate-config  
RUN rm /.jupyter/jupyter_notebook_config.py  
ADD jupyter_notebook_config.py /.jupyter/  

