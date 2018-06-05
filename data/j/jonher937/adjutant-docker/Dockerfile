FROM alpine:latest  
LABEL maintainer="Jonathan Herlin <jonte@jherlin.se>"  
  
COPY set_config.sh /opt/set_config.sh  
RUN apk add --no-cache python \  
git \  
py-pip \  
mysql-client \  
mariadb-dev \  
build-base \  
linux-headers \  
python-dev \  
bash \  
&& pip install --upgrade pip \  
&& git clone https://git.openstack.org/openstack/adjutant /opt/adjutant \  
&& cd /opt/adjutant \  
&& pip install -r requirements.txt \  
&& python setup.py develop \  
&& /usr/bin/adjutant-api migrate  
  
WORKDIR /opt/adjutant  
ENTRYPOINT ["/bin/bash", "/opt/set_config.sh"]  
CMD ["/usr/bin/adjutant-api", "runserver", "0.0.0.0:5050"]  
# To be implemented: RUN ln -sf /dev/stdout /var/log/nginx/access.log  

