FROM python:3-alpine  
MAINTAINER Ram Zallan (ram@csh.rit.edu)  
  
# Install additional system packages required for certain python dependencies  
RUN apk add --no-cache postgresql-dev libffi-dev python-dev gcc musl-dev
openssl-dev openldap-dev ca-certificates && \  
update-ca-certificates  
  
# Configure OpenLDAP to use the system trusted CA Store  
RUN echo "tls_cacertdir /etc/ssl/certs" >> /etc/openldap/ldap.conf  
  
# Add application user  
RUN adduser -S map && \  
mkdir -p /opt/map  
  
# Add files and set permissions  
ADD . /opt/map  
RUN chown -R map /opt/map  
WORKDIR /opt/map  
  
# Install python dependencies  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Drop privileges  
USER map  
  
# Expose default port  
EXPOSE 8080  
# Run application with Gunicorn  
CMD gunicorn --workers=2 --bind
${MAP_SERVER_IP:-0.0.0.0}:${MAP_SERVER_PORT:-8080} app  

