FROM postgres:9.6.3  
MAINTAINER Matt Beedle <me@mattbeedle.name>  
  
USER root  
RUN apt-get update  
RUN apt-get install -q -y --force-yes \  
cron \  
gnupg \  
python-pip \  
gzip  
  
# AWS Command Line Interface  
RUN pip install awscli==1.9.15  
  
# Note that because cron does not seem to know about Docker's environment  
# variables, we have to read them in from a file that we write out  
# in entrypoint.sh at runtime.  
RUN echo "0 */4 * * * env - \\`cat /tmp/env.sh\\` /bin/bash -c '(cd /code &&
sh run-backup.sh) >> /code/backups-cron.log 2>>\&1'" | crontab -  
  
RUN mkdir -p /code  
WORKDIR /code  
ADD entrypoint.sh /code/entrypoint.sh  
ADD run-backup.sh /code/run-backup.sh  
RUN chmod +x /code/entrypoint.sh  
  
ENTRYPOINT ["sh", "entrypoint.sh"]  
CMD [""] # overrides the default from image we inherited from  

