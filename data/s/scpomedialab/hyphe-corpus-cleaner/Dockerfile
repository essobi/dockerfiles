FROM python:2.7-alpine  
  
COPY requirements.txt /app/requirements.txt  
  
RUN apk --update add gcc musl-dev curl ssmtp mailx \  
&& pip install --no-cache-dir --requirement /app/requirements.txt \  
&& curl -sL https://github.com/michaloo/go-cron/releases/download/v0.0.2/go-
cron.tar.gz | tar -x -C /usr/local/bin \  
&& apk del gcc musl-dev curl \  
&& rm /var/cache/apk/*  
  
  
COPY clean_old_corpora.py /clean_old_corpora.py  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  
  

