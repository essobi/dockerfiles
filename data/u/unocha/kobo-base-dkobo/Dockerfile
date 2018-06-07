FROM unocha/kobo-base-kobos:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
RUN mkdir -p /srv/src && \  
cd /srv/src && \  
git clone https://github.com/kobotoolbox/dkobo.git -b master koboform && \  
cd /srv/src/koboform && \  
pip install -r requirements.txt && \  
pip install raven==5.2.0 && \  
pip install newrelic && \  
npm --no-color install \  
yuglify && \  
chown -R wsgi /srv/src/koboform  

