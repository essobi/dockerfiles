FROM sentry:8.20  
RUN pip install https://github.com/getsentry/sentry-auth-
google/archive/master.zip  
RUN sed -i -e '4 a echo GOOGLE_CLIENT_ID = \\\"$GOOGLE_CLIENT_ID\\\" >>
/etc/sentry/sentry.conf.py' \  
-e '4 a echo GOOGLE_CLIENT_SECRET = \\\"$GOOGLE_CLIENT_SECRET\\\" >> /etc/sentry/sentry.conf.py' /entrypoint.sh  

