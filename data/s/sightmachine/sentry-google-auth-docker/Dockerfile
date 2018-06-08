FROM sentry:8.17  
COPY sentry.conf.py /etc/sentry/  
  
# Have to install specific hash see issue:
https://github.com/getsentry/sentry-auth-google/issues/21  
RUN pip install git+git://github.com/getsentry/sentry-auth-google.git@0.1.0  

