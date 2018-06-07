FROM itsalgeria/insidjam:latest  
MAINTAINER Itsolutions  
  
# Project's specifics packages  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-shapely nano htop \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./requirements.txt /opt/odoo/  
RUN cd /opt/odoo && pip install -r requirements.txt  
RUN pip install XlsxWriter ftputil  
  
ENV TERM xterm  
  
ENV TZ=Etc/UTC  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
&& dpkg-reconfigure -f noninteractive tzdata  
  
# --- workers bugfix: gevent v1.1.0 to prevent using SSLv3  
COPY ./gevent-1.1.0.tar.gz /opt/odoo/  
RUN cd /opt/odoo && pip install -Iv gevent-1.1.0.tar.gz  
  

