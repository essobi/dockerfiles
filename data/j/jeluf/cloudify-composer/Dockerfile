FROM ubuntu  
MAINTAINER Jens Frank <jf@mormo.org>  
RUN apt-get update -y && apt-get install -y gcc curl python2.7 python2.7-dev
libpython2.7-dev libffi6 libffi-dev openssl libssl-dev  
RUN curl https://bootstrap.pypa.io/get-pip.py | python2.7 && pip install
virtualenv && pip install \--upgrade ndg-httpsclient  
RUN curl https://raw.githubusercontent.com/cloudify-cosmo/get-
cloudify.py/master/get-cloudify-composer.py | python2.7  
  
CMD /opt/cloudify-composer/nodejs/bin/node /opt/cloudify-composer/blueprint-
composer/package/server.js  
EXPOSE 3000  

