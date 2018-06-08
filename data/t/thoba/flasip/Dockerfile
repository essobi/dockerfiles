FROM python:2.7  
LABEL maintainer="lose.thoba@gmail.com"  
  
RUN apt-get update -y --fix-missing && \  
apt-get upgrade -y && \  
pip install -U pip && \  
mkdir code  
COPY requirements.txt /code  
WORKDIR /code  
RUN pip install -r requirements.txt  
COPY . /code  
CMD ["python", "main.py"]  

