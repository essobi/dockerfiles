FROM python:3.6.0  
ENV PYTHONBUFFERED 1  
ENV DATABASE_URL postgres://user:pass@host:5432/db  
  
ENV SECRET_KEY 'ah_f*z03ogus3mzgno)a)(!0!&hd$0(r*$ld78tqmtdi-t96%%'  
ENV RDEC_DEBUG False  
ENV RDEC_ALLOWED_HOSTS '*'  
ENV LOG_LEVEL INFO  
  
# If AWS_ACCESS_KEY_ID is empty - fall back to local/whitenoise hosting  
# Otherwise - S3 bucket  
ENV AWS_ACCESS_KEY_ID ""  
ENV AWS_SECRET_ACCESS_KEY ""  
ENV AWS_STORAGE_BUCKET_NAME ""  
ENV AWS_MEDIA_BUCKET_NAME ""  
ENV RDEC_LEAGUE_NAME ""  
ENV RDEC_RECENT_EVENT_CUTOFF_DAYS ""  
ENV RDEC_MAIL_FROM_ADDRESS ""  
WORKDIR /app  
ADD . .  
RUN pip install -r requirements.txt  
RUN python manage.py collectstatic --noinput  
  
CMD ["gunicorn", "rdecsite.wsgi", "--log-file", "-", "-b", "0.0.0.0:8000", "--
access-logfile", "-"]  
EXPOSE 8000  

