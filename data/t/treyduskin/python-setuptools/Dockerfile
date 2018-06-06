FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y python-pip createrepo rpm dpkg-dev
git  
  
RUN pip install setuptools-scm && pip install --upgrade setuptools  
  
VOLUME /build  
  
#COPY . /build/  
ENTRYPOINT ["python", "setup.py"]  
  
WORKDIR /build  
ENV HOME=/build/  
  

