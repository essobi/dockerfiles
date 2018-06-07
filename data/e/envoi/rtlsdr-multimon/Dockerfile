# derive from our baseimage  
FROM envoi/rtlsdr-base:latest  
  
MAINTAINER Anton S. <anton@env.sh>  
LABEL Description="RTLSDR Multimon-ng in Docker"  
LABEL Vendor="Envoi"  
LABEL Version="0.0.1"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends qt4-qmake libpulse-dev
libx11-dev lighttpd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ldconfig  
  
RUN git clone \--depth 1 --progress git://github.com/EliasOenal/multimon-
ng.git /tmp/multimon-ng  
  
RUN mkdir /tmp/multimon-ng/build  
  
WORKDIR /tmp/multimon-ng/build  
RUN qmake ../multimon-ng.pro PREFIX=/usr/local  
RUN make  
RUN make install  
  
RUN mkdir /var/www/pager/  
RUN chmod 777 /var/www/pager/  
  
EXPOSE 8080  
VOLUME ["/var/www/pager"]  
  
WORKDIR /var/www  
RUN git clone \--depth 1 --progress https://github.com/derekeder/csv-to-html-
table /var/www/csv-to-html-table  
COPY index.html /var/www  
  
COPY ./run.sh /  
ENTRYPOINT ["/run.sh"]  

