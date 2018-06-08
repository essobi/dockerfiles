FROM ubuntu:latest  
RUN apt-get update -y  
RUN apt-get install -y libxslt-dev python3-dev build-essential zlib1g-dev pkg-
config python3-pip  
COPY . /app  
WORKDIR /app  
RUN pip3 install wheel && pip3 install -r requirements.txt  
ENV PYTHONPATH=.  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
EXPOSE 4444  
CMD ["asphalt", "run", "-l", "uvloop", "config.yml"]

