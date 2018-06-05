FROM alpine:3.5  
#File Author / Maintainer  
MAINTAINER Troy Kelly  
  
RUN apk update && \  
apk add --no-cache git && \  
apk add --update \  
python \  
python-dev \  
py-pip \  
libffi-dev \  
openldap-dev \  
build-base \  
mariadb-dev && \  
pip install -U pip && \  
rm -rf /var/cache/apk/*  
  
# Install Virtualenv  
RUN pip install virtualenv  
  
# Create a new directory where the virtual environment will be created and add
the requirements file.  
RUN git clone https://github.com/ngoduykhanh/PowerDNS-Admin.git /app  
  
WORKDIR /app  
  
RUN virtualenv flask && \  
source ./flask/bin/activate && \  
pip install MySQL-python && \  
pip install -r requirements.txt && \  
cp config_template.py config.py && \  
sed -i "s|LOG_FILE = 'logfile.log'|LOG_FILE = ''|g" /app/config.py; \  
sed -i "s|BASIC_ENABLED = True|BASIC_ENABLED = False|g" /app/config.py; \  
sed -i "s|SIGNUP_ENABLED = True|SIGNUP_ENABLED = False|g" /app/config.py; \  
sed -i "s|PDNS_VERSION = '3.4.7'|PDNS_VERSION = '4.0.4'|g" /app/config.py; \  
sed -i "s|PRETTY_IPV6_PTR = False|PRETTY_IPV6_PTR = True|g" /app/config.py  
  
EXPOSE 9393  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  

