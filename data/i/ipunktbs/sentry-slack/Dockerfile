FROM sentry:8.18.0  
RUN echo "SENTRY_FEATURES['auth:register'] =
os.environ.get('SENTRY_ALLOW_REGISTRATION') or 'True'" >>
/etc/sentry/sentry.conf.py  

