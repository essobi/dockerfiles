FROM debian:wheezy  
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>  
  
RUN set -x && \  
apt-get update && apt-get install -y --no-install-recommends \  
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
RUN /tmp/gaesdk_download.py 1.9.40 && \  
rm -rf /tmp/*  
ENV PATH /opt/google_appengine:$PATH  
  
WORKDIR /src  
  
EXPOSE 8000 8001 8002  
CMD ["python", "manage.py", "runserver"]  
  
ONBUILD ADD /src /src  
ONBUILD RUN pip install -r /src/requirements.txt -t /src/sitepackages  

