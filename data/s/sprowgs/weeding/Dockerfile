FROM buildpack-deps:jessie  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
#ENV PYTHON_PIP_VERSION 7.0.3  
RUN apt-get update && apt-get install -y python-dev netcat python-pip  
  
#RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2  
RUN pip install --upgrade pip  
  
RUN pip install gunicorn  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install -r requirements.txt  
COPY . /usr/src/app

