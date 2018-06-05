FROM nginx:mainline  
  
ENV SUPERVISOR_VERSION 3.3.0  
RUN set -x \  
&& apt-get update && apt-get install --no-install-recommends -yqq \  
dnsmasq \  
wget \  
python-setuptools \  
&& wget
https://github.com/Supervisor/supervisor/archive/${SUPERVISOR_VERSION}.tar.gz
\  
&& tar -xvf ${SUPERVISOR_VERSION}.tar.gz \  
&& cd supervisor-${SUPERVISOR_VERSION} && python setup.py install \  
&& apt-get clean autoclean && apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  
  

