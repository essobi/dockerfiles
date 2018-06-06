FROM centos:latest  
MAINTAINER Ram Parashar <ram.parashar@voyant.com>  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"  
RUN python get-pip.py  
  
RUN yum -y install git  
  
RUN mkdir /apps  
  
WORKDIR /apps  
ENV GIT_SSL_NO_VERIFY=1  
RUN git clone https://github.com/anpisolutions/chatterbot.git  
  
WORKDIR chatterbot  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python"]  
CMD ["app.py"]

