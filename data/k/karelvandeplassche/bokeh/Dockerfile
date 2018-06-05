#FROM osixia/web-baseimage:1.0.0  
FROM osixia/light-baseimage:1.1.1  
MAINTAINER Karel van de Plassche <karelvandeplassche@gmail.com>  
  
#RUN /container/tool/add-multiple-process-stack \  
# && /container/tool/add-service-available :nginx \  
RUN apt-get update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-
recommends \  
# vim \  
# git \  
# build-essential \  
# libyaml-dev \  
python3 \  
python3-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip3 install --upgrade pip  
  
RUN pip install setuptools  
  
RUN pip install \  
bokeh==0.12.7 \  
tornado==4.3  
  
# Add service directory to /container/service  
ADD service /container/service  
  
# Use baseimage install-service script  
# https://github.com/osixia/docker-light-
baseimage/blob/stable/image/tool/install-service  
RUN /container/tool/install-service  
  
# Add default env variables  
ADD environment /container/environment/99-default  
  
# Print bokeh version information  
RUN python3 -c "import tornado; print('tornado version=' + tornado.version)"  
RUN bokeh info  

