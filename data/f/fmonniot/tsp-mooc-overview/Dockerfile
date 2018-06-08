# Use same base as postgres to minimize total size  
FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y python curl \  
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python  
  
# Force stdin, stdout and stderr to be totally unbuffered  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /app  
WORKDIR /app  
  
ADD requirements.txt /app/  
  
RUN pip install -r requirements.txt  
  
ADD . /app/  
  
EXPOSE 5000  
CMD ["python", "app.py"]  

