FROM r-base:3.4.0  
  
MAINTAINER kirillseva "https://github.com/kirillseva"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
libxml2-dev \  
libpq-dev \  
postgresql \  
postgresql-contrib \  
libtiff5-dev \  
libgmp-dev \  
libssl-dev \  
s3cmd \  
git \  
curl \  
cmake \  
python2.7 \  
python-pip \  
python3-pip \  
libatlas-dev \  
liblapack-dev \  
build-essential \  
python-dev \  
gfortran \  
libblas-dev \  
python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN install2.r --error \  
\--deps TRUE \  
curl \  
jsonlite \  
httr \  
yaml \  
digest \  
crayon \  
remotes  
  
RUN installGithub.r \  
robertzk/lockbox@0.2.4.7  
  
RUN mkdir -p /dev  
RUN pip install darts.util.lru==0.5 Flask==0.10.1 gunicorn==19.3.0
itsdangerous==0.24 Jinja2==2.8 MarkupSafe==0.23 numpy==1.9.3 scipy==0.16.0
scikit-learn==0.17 Werkzeug==0.10.4 wheel==0.24.0  
# xgboost  
RUN cd /dev && git clone --recursive https://github.com/kirillseva/xgboost.git
\  
&& cd xgboost && git checkout 0.6.0.9012 && make -j4 && cd python-package &&
python setup.py install  
  
CMD ["R"]  

