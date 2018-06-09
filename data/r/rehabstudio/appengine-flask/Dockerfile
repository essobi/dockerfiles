FROM debian:wheezy  
MAINTAINER Dan Porter <dan.porter@rehabstudio.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-transport-https \  
build-essential \  
libxslt1-dev \  
mysql-client \  
libmysqlclient-dev \  
ipython \  
sqlite3 \  
python-imaging \  
python-numpy \  
python-dev \  
python-pip \  
git \  
sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Download and install the Appengine Python SDK  
ADD gaesdk_download.py /tmp/gaesdk_download.py  
RUN /tmp/gaesdk_download.py 1.9.35 && \  
rm -rf /tmp/*  
ENV PATH /opt/google_appengine:$PATH  
  
ADD src /src  
WORKDIR /src  
  
RUN pip install -r requirements.txt -t lib  
  
EXPOSE 8080 8081 8082  
CMD ["make", "run"]  

