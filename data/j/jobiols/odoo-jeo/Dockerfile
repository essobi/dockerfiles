FROM adhoc/odoo-ar:8.0  
MAINTAINER Jorge Obiols <jorge.obiols@gmail.com>  
  
USER root  
  
# markdown support  
RUN git clone \--depth 1 https://github.com/jobiols/Python-Markdown.git
/python-markdown  
RUN cd /python-markdown && python setup.py install  
  
# pysftp support  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-pip \  
&& pip install pysftp  
  
COPY ./entrypoint.sh /opt/odoo/resources/entrypoint.sh  
  
USER odoo  

