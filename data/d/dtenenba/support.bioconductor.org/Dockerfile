FROM ubuntu:14.04  
MAINTAINER dtenenba@fredhutch.org  
  
EXPOSE 8080  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get dist-upgrade -y  
  
# FIXME, merge this with above  
RUN apt-get install -y \  
curl \  
libpq-dev \  
postgresql-client \  
python \  
python-dev  
  
ADD default.env /conf/default.env  
  
#VOLUME /biostar-central  
#RUN mkdir /biostar-central  
RUN curl https://bootstrap.pypa.io/get-pip.py | python && \  
/usr/local/bin/pip install --upgrade google-api-python-client  
  
RUN cd /tmp && curl -O \  
https://raw.githubusercontent.com/Bioconductor/support.bioconductor.org/master/conf/requirements/base.txt
&& \  
pip install --upgrade -r base.txt && cd /  
  
RUN pip install --upgrade ipython elasticsearch waitress whitenoise  
  
WORKDIR /biostar-central  
  
ADD start.sh /conf/start.sh  
  
#CMD source /conf/default.env && ./biostar.sh init import index run  
CMD /conf/start.sh  

