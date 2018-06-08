FROM debian:jessie  
  
MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>  
LABEL Version="1.0" Description="Run a simple web app to list directory
contents"  
  
RUN apt-get clean && apt-get update -qq && apt-get install -qq -y \  
git \  
openssh-client \  
python3 \  
python3-dev \  
python3-pip \  
virtualenv \  
build-essential  
  
RUN cd /srv ; git clone https://github.com/MiloCasagrande/simple-storage.git  
RUN mkdir -p /srv/storage-env  
  
ENV PYTHONUSERBASE /srv/storage-env  
RUN pip3 install -q -r /srv/simple-storage/requirements.txt --user  
  
COPY storage.ini /srv  
COPY simple-storage.cfg /srv  
  
COPY start.sh /  
RUN chmod +x /start.sh  
  
EXPOSE 5000  
CMD ["/start.sh"]  

