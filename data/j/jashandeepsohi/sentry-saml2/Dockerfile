FROM sentry:8.22.0  
LABEL maintainer="Jashandeep Sohi <jashandeep.s.sohi@gmail.com>"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libxmlsec1-dev \  
pkg-config  
  
COPY . /usr/src/sentry-saml2  
  
WORKDIR /usr/src/sentry-saml2  
  
RUN pip install -r requirements.txt  
  
RUN cat sentry.conf.py >> $SENTRY_CONF/sentry.conf.py  

