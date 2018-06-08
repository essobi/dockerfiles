ARG BASE_VERSION=latest  
  
FROM jonasprogrammer/nipapd:${BASE_VERSION}  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libev-dev \  
&& pip --no-input install bjoern \  
&& rm -rf /var/lib/apt/lists/* \  
&& adduser --gecos '' \--disabled-login --disabled-password --no-create-home
--home /var/cache/nipap-www nipap-www  
  
COPY nipap/nipap-www /nipap/www  
COPY nipap/pynipap /nipap/pynipap  
WORKDIR /nipap/www  
RUN cd /nipap/pynipap && python setup.py install && cd /nipap/www \  
&& pip --no-input install -r requirements.txt \  
&& python setup.py install  
  
EXPOSE 8080  
ENV NIPAPD_PORT=1337 \  
AUTH_DEFAULT=true AUTH_BACKEND=local AUTH_CACHE=3600 \  
AUTH_BACKEND_local_type=SqliteAuth
AUTH_BACKEND_local_db_path=/etc/nipap/local_auth.db  
  
COPY www-bjoern.py entrypoint-www.sh /nipap/www/  
  
ENTRYPOINT ["/nipap/www/entrypoint-www.sh"]  
CMD ["/nipap/www/www-bjoern.py"]  

