FROM debian:wheezy  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install adduser python python-pip python-
requests \  
&& apt-get clean  
  
RUN pip install radicale  
  
ADD default_radicale_config.conf /default_radicale_config.conf  
  
RUN mkdir /radicale  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
RUN addgroup --quiet --system radicale  
RUN adduser --home /radicale --group --quiet --system radicale  
  
RUN chown radicale:radicale -R /radicale && chmod 755 -R /radicale  
  
USER radicale  
  
EXPOSE 5232  
VOLUME /var/logs  
VOLUME /radicale  
  
CMD []  
ENTRYPOINT ["/launcher.py"]  

