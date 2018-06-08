FROM ubuntu:trusty  
MAINTAINER Chris Trotman <chris@trotman.io>  
  
RUN apt-get update  
RUN apt-get install -y python python-virtualenv  
RUN mkdir /venv  
RUN virtualenv /venv/unifi  
RUN /venv/unifi/bin/pip install unifi  
RUN sed -i 's/SSLv3/TLSv1/g' /venv/unifi/lib/python2.7/site-
packages/unifi/controller.py  
  
ENV UNIFI_CONTROLLER localhost  
ENV UNIFI_USERNAME admin  
ENV UNIFI_PASSWORD admin  
ENV UNIFI_VERSION v3  
ENV UNIFI_SITE default  
ENV UNIFI_MIN_SNR 28  
CMD /venv/unifi/bin/unifi-low-snr-reconnect \  
-c $UNIFI_CONTROLLER \  
-u $UNIFI_USERNAME \  
-p $UNIFI_PASSWORD \  
-v $UNIFI_VERSION \  
-s $UNIFI_SITE \  
\--minsnr $UNIFI_MIN_SNR  

