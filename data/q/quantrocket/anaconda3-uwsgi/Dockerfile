# when upgrading anaconda3, consider doing so in quantrocket/jupyter as well  
# to facilitate layer caching  
FROM continuumio/anaconda3:4.4.0  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
# N.B: Don't call this UWSGI_VERSION:
https://github.com/unbit/uwsgi/issues/898  
# However, we do set UWSGI_WORKERS and UWSGI_THREADS here  
ENV UWSGIVERSION=2.0.15 \  
HOUSTON_URL=http://houston \  
IBAPI_VERSION=973.06 \  
UWSGI_WORKERS=1 \  
UWSGI_THREADS=2 \  
SQLITE3_VERSION=3220000  
RUN apt-get update && apt-get install -y \  
unzip \  
build-essential \  
libpcre3 \  
libpcre3-dev \  
&& curl --fail --output /tmp/uwsgi.zip
https://codeload.github.com/unbit/uwsgi/zip/${UWSGIVERSION} \  
&& cd /tmp \  
&& unzip uwsgi.zip \  
&& mv uwsgi-${UWSGIVERSION} uwsgi \  
&& rm uwsgi.zip  
  
# We need sqlite3 3.20.0+ to allow the DATE function in indexes  
#
https://sqlite.org/deterministic.html#special_case_processing_for_date_time_functions  
RUN curl --fail --output /tmp/sqlite3.tar.gz
"https://www.sqlite.org/2018/sqlite-autoconf-${SQLITE3_VERSION}.tar.gz" \  
&& cd /tmp \  
&& tar xvfz sqlite3.tar.gz \  
&& cd sqlite-autoconf-${SQLITE3_VERSION} \  
&& ./configure --prefix=/opt/conda \  
&& make \  
&& make install \  
&& cd / \  
&& rm -r /tmp/sqlite-autoconf-* \  
&& rm /tmp/sqlite3.tar.gz  
  
# Install ibapi  
RUN curl --fail --output /tmp/ibapi.zip
http://interactivebrokers.github.io/downloads/twsapi_macunix.${IBAPI_VERSION}.zip
\  
&& cd /tmp \  
&& unzip ibapi.zip \  
&& cd IBJts/source/pythonclient \  
&& /bin/bash -c "source activate /opt/conda" \  
&& pip install . \  
&& /bin/bash -c "source deactivate" \  
&& apt-get remove -y unzip \  
&& cd /tmp \  
&& rm -r IBJts \  
&& rm ibapi.zip  
  
EXPOSE 80  
COPY uwsgi /etc/uwsgi  
COPY build.ini /tmp/uwsgi/buildconf/quantrocket.ini  
COPY build_dev.ini /tmp/uwsgi/buildconf/quantrocket_dev.ini  
COPY qrocket /tmp/uwsgi/qrocket  
COPY qrocket/servicename.py /opt/conda/bin/servicename  
COPY build*.sh /tmp/  
  
RUN chmod +x /tmp/build*.sh \  
&& chmod +x /opt/conda/bin/servicename \  
&& mkdir -p /var/tmp/uwsgi/spool  
  
# Install Flask et al  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install flask==0.12 \  
&& pip install dnspython==1.15.0 \  
&& pip install uwsgi-tools==1.0.3 \  
&& pip install flask-restful==0.3.5 \  
&& pip install webargs==1.6.0 \  
&& pip install csvkit==1.0.2 \  
&& pip install ibpythonic \  
&& pip install quantrocket-client \  
&& /bin/bash -c "source deactivate"  
  
ONBUILD CMD ["uwsgi-quantrocket", "--ini", "/etc/uwsgi/uwsgi.ini"]  

