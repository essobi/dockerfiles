FROM ubuntu:latest  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install wget python-pip python-dev  
  
RUN pip install Flask  
RUN pip install flask-cors  
  
WORKDIR /tmp/downloads  
  
RUN wget http://atlee.ca/software/poster/dist/0.8.1/poster-0.8.1-py2.7.egg &&
\  
easy_install poster-0.8.1-py2.7.egg && \  
rm poster-0.8.1-py2.7.egg  
  
RUN wget
https://pypi.python.org/packages/bc/d6/960acce47ee6f096345fe5a7d9be7708135fd1d0713571836f073efc7393/suds-0.4.tar.gz
&& \  
tar xvf suds-0.4.tar.gz && \  
cd suds-0.4 && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rvf suds-0.4  
  
RUN mkdir /appl && \  
mkdir /appl/api_wssso  
  
COPY . /appl/api_wssso  
  
EXPOSE 5000  
CMD ["python", "/appl/api_wssso/api.py"]  

