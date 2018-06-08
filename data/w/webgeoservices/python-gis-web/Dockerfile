FROM buildpack-deps:jessie  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.1  
RUN apt-get update && apt-get install -y libgeos-dev libgdal-dev \  
python-gdal python-dev netcat  
  
RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2  
RUN pip install --upgrade pip==$PYTHON_PIP_VERSION  
  
RUN pip install gunicorn mapnik==0.1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install -r requirements.txt  
ONBUILD COPY . /usr/src/app  

