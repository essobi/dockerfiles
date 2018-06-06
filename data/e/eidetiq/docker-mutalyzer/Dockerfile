FROM python:2.7  
MAINTAINER Pasha Katsev <pkatsev@gmail.com>  
  
# workspace  
RUN mkdir -p /data/cache  
WORKDIR /data  
  
# dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpq-dev \  
libxml2-dev \  
libxslt-dev \  
python-dev \  
swig  
  
# dl/extract mutalyzer release  
RUN mkdir mutalyzer \  
&& curl -fsSL \  
https://github.com/mutalyzer/mutalyzer/archive/v2.0.17.tar.gz \  
| tar zxC mutalyzer --strip=1  
  
# python env  
RUN pip install -U setuptools pip numpy psycopg2 \  
&& pip install -r mutalyzer/requirements.txt \  
&& pip install mutalyzer/  
  
# settings  
ENV MUTALYZER_SETTINGS /data/mutalyzer/settings.py  
COPY etc/settings.py $MUTALYZER_SETTINGS  
  
# scripts  
COPY bin/* /data/  
  
VOLUME ["/data/cache"]  
  
ENTRYPOINT ["./entrypoint.sh"]  
  
CMD ["mutalyzer-admin", "assemblies", "list"]  

