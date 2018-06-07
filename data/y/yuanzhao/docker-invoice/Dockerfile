FROM centos:latest  
MAINTAINER Yuan Zhao "https://github.com/yuanzhaoYZ"  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y --setopt=tsflags=nodocs install httpd  
RUN yum -y install wget  
RUN yum -y install poppler-utils #pdftotext  
RUN yum -y install python-devel # for python-levenshtein  
RUN yum -y groupinstall 'Development Tools' # for python-levenshtein  
RUN yum -y --enablerepo epel-testing install tesseract.x86_64  
RUN yum -y install ghostscript  
RUN yum -y install ImageMagick  
RUN cd /tmp/;wget https://bootstrap.pypa.io/get-pip.py;python get-pip.py  
RUN pip install Pillow;pip install python-levenshtein;pip install pyap;pip
install pypdfocr  
RUN mkdir /home/data;mkdir /home/output;cd /home  
ADD *.py /home/  
ADD run.sh /home  
ADD data/*.pdf /home/data/  
  
RUN chmod -v +x /home/run.sh  
EXPOSE 80  
WORKDIR /home  

