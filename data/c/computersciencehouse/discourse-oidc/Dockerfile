# computersciencehouse/discourse-oidc  
FROM python:3-alpine  
MAINTAINER Steven Mirabito (smirabito@csh.rit.edu)  
  
# Install additional system packages required for certain python dependencies  
RUN apk add --no-cache libffi-dev python-dev gcc musl-dev openssl-dev ca-
certificates && \  
update-ca-certificates  
  
# Add application user  
RUN adduser -S sso && \  
mkdir -p /opt/sso  
  
# Add files and set permissions  
ADD . /opt/sso  
RUN chown -R sso /opt/sso  
WORKDIR /opt/sso  
  
# Install python dependencies and application  
RUN pip install --no-cache-dir -r requirements.txt && python setup.py install  
  
# Drop privileges  
USER sso  
  
# Expose default port  
EXPOSE 8080  
# Run application with Gunicorn  
CMD gunicorn --workers=2 --bind
${SSO_SERVER_IP:-0.0.0.0}:${SSO_SERVER_PORT:-8080} DiscourseOIDC  

