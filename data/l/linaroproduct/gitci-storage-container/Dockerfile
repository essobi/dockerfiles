FROM debian:stretch  
  
MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>  
LABEL Version="1.0" Description="Run the git://ci storage app"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get clean && apt-get update -qq && apt-get install -qq -y --no-
install-recommends \  
ca-certificates \  
git \  
&& git clone https://github.com/linaro-product/gitci-storage.git /srv/gitci-
storage \  
&& apt-get purge -y --auto-remove git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /srv/gitci-storage-env  
ENV PYTHONUSERBASE /srv/gitci-storage-env  
RUN apt-get clean && apt-get update -qq && apt-get install -qq -y --no-
install-recommends \  
build-essential \  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
python3-virtualenv \  
python3-wheel \  
&& pip3 install -r /srv/gitci-storage/requirements.txt --user \  
&& apt-get purge -y --auto-remove build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY gitci-storage-uwsgi.ini /srv  
COPY gitci-storage.cfg /srv  
  
EXPOSE 5050  
WORKDIR /srv/gitci-storage-env/bin  
CMD ["./uwsgi", "--ini", "/srv/gitci-storage-uwsgi.ini"]  

