FROM unit9/base:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install --yes --no-install-recommends \  
build-essential \  
python \  
python-all-dev \  
python-pip \  
python-wheel \  
&& apt-get clean \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
WORKDIR /app  
  
RUN pip install --upgrade pip  
ADD requirements.txt /app  
RUN pip install -r requirements.txt  
  
RUN mkdir /app/tests  
ADD run /etc/service/locust/run  
  
EXPOSE 8089 5557 5558  

