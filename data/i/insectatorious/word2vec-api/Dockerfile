FROM ubuntu:16.04  
  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
libblas-dev \  
checkinstall \  
libblas-doc \  
checkinstall \  
liblapacke-dev \  
checkinstall \  
liblapack-doc \  
checkinstall \  
gfortran \  
python3-dev \  
python3-pip  
  
RUN /usr/bin/yes | pip3 install -U \  
Cython \  
numpy \  
ujson \  
gunicorn \  
gensim \  
sklearn \  
scikit-learn  
  
# Build from source  
RUN /usr/bin/yes | pip3 install --no-binary :all: falcon falcon-cors  
  
WORKDIR /usr/src/app  
COPY *.py ./  
  
EXPOSE 8080  
CMD ["gunicorn", \  
"--reload", \  
"--workers", "2", \  
"--threads", "2", \  
"--bind", "0.0.0.0:8080", \  
"app:api"]

