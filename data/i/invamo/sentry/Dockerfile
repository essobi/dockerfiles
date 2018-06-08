FROM sentry:8.18.0  
  
MAINTAINER Tristan Holl  
  
# Install Plugins  
RUN pip install sentry-plugins  
  
# Copy custom sentry config  
COPY sentry.conf.py /etc/sentry/  
  
# Remove old organization logo  
RUN rm /usr/local/lib/python2.7/site-
packages/sentry/static/sentry/images/default-organization-logo.png  
# Copy new organization logo  
COPY logo.png /usr/local/lib/python2.7/site-
packages/sentry/static/sentry/images/default-organization-logo.png  

