FROM winsent/opendronemap:0.2.1  
MAINTAINER Seth Fitzsimmons <seth@mojodna.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
build-essential \  
git \  
libgdal-dev \  
python-dev \  
python-numpy \  
python-pillow \  
python-pip \  
python-setuptools \  
python-wheel && \  
apt-get clean  
  
COPY requirements.txt /app/requirements.txt  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt && \  
pip install -U gevent gunicorn && \  
rm -rf /root/.cache  
  
COPY . /app  
  
# Add DJI Phantom 4 sensor  
RUN sed -i '2i\ "DJI FC330": 6.25,'
/code/SuperBuild/src/opensfm/opensfm/data/sensor_data.json  
  
# override this accordingly; should be 2-4x $(nproc)  
ENV WEB_CONCURRENCY 4  
EXPOSE 8000  
USER nobody  
VOLUME /app/projects  
VOLUME /app/uploads  
  
ENTRYPOINT ["gunicorn", "-k", "gevent", "-b", "0.0.0.0", "--timeout", "300", "
--access-logfile", "-", "app:app"]  

