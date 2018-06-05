FROM python:2  
RUN apt-get -y update  
RUN pip install flask  
  
ADD . /src  
WORKDIR /src  
  
EXPOSE 5000  
CMD ["python", "/src/app.py"]

