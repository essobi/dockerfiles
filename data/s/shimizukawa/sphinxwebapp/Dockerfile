FROM python:2.7  
# install curl and fluentd deps  
##### python:2.7 has curl already.  
#RUN apt-get update && apt-get install -y curl && apt-get clean  
# install mercurial  
RUN pip install -q mercurial  
  
# install optional packages  
RUN pip install -q pillow whoosh gunicorn python-levenshtein  
  
# install sphinx  
RUN pip install -q "sphinx>=1.3a0"  
  
# install sphinx webapp  
RUN pip install -q hg+https://bitbucket.org/shimizukawa/sphinx-demo-webapp  
  
RUN mkdir -p /var/sphinxweb /doc/source /doc/build  
ADD ./config /app/config  
ADD ./bin /app/bin  
WORKDIR /doc  
  
ENV SPHINXWEB_SETTINGS /app/config/sphinxweb.cfg  
#ENV SPHINXWEB_PORT 5000 # default is 5000  
#ENV SPHINXWEB_WORKERS 2 # default is number of cpu core  
CMD /bin/bash /app/bin/start  
  

