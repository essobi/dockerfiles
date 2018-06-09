FROM iwsaas/python:latest  
RUN yum install -y swig openssl-devel m2crypto python-devel libxml2-devel
libxmlsec1-devel xmlsec1-devel gcc gcc-c++ xmlsec1-devel xmlsec1-gcrypt
xmlsec1-gcrypt-devel xmlsec1-openssl-devel python-m2ext libtool-ltdl-devel  
RUN pip install M2Crypto dm.xmlsec.binding isodate defusedxml python-saml  
RUN yum install wget unzip -y  
RUN wget https://github.com/jianwei/docker/archive/master.zip  
RUN unzip master.zip  
RUN pip install bottle  
RUN cp docker-master/sample/hello.py ./  
CMD ["python","hellow.py"]  
  

