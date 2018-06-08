FROM frolvlad/alpine-python3  
MAINTAINER Gladyshev Bogdan  
  
ADD ./requirements.txt /requirements.txt  
# Install flask  
RUN pip3 install --upgrade pip \  
&& pip3 install -r /requirements.txt  
  
ADD . /flask  
  
EXPOSE 8890  
WORKDIR /flask  
  
CMD 'python3' 'main.py'

