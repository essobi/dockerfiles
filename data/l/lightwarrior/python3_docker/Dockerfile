FROM python:3.4  
MAINTAINER Werner Raath <wraath@csir.co.za>  
  
ARG SUEXEC_VER=0.2  
ARG SUEXEC_DOWNLOAD_URL=https://github.com/ncopa/su-
exec/archive/v${SUEXEC_VER}.tar.gz  
  
ENV PYTHONPATH=/usr/local/lib/python3.4/site-packages  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-client \  
gdal-bin \  
libgdal-dev \  
postgis \  
python3-gdal \  
python3-pyproj \  
python-numpy \  
python-scipy \  
ipython \  
python-pyexiv2 \  
libatlas-dev libatlas3gf-base \  
curl python3-shapely python3-jinja2 python3-yaml \  
&& pip3 install --upgrade pip \  
&& echo "${SUEXEC_DOWNLOAD_URL}" \  
&& curl -k -fsSL -o /tmp/suexec.tgz "${SUEXEC_DOWNLOAD_URL}" \  
&& cd /tmp \  
&& tar xvf suexec.tgz \  
&& cd "/tmp/su-exec-${SUEXEC_VER}" \  
&& make \  
&& cp -af su-exec /usr/bin/ \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& ln -fs /usr/bin/python3.4 /usr/bin/python  
  
ENV PATH=/usr/bin:$PATH  
  
# Include /urr/bin to use correct python3  
# Base image uses /usr/local/bin/python3 which can't fund python3-* modules  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

