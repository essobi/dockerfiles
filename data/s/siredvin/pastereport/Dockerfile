FROM frolvlad/alpine-python3  
MAINTAINER Gladyshev Bogdan  
  
# Install flask  
RUN pip3 install --upgrade pip \  
&& pip3 install flask  
  
ADD . /flask  
  
EXPOSE 8877  
ENV UPLOAD_DIRECTORY /flask/static  
WORKDIR /flask  
  
CMD 'python3' 'PasteReport.py'

