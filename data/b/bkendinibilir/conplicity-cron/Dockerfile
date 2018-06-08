FROM alpine  
  
ARG CONPLICITY_VERSION=0.24.2  
# Default: backup every night at 3:30 am  
ENV CONPLICITY_CRON_SCHEDULE="30 3 * * *"  
ENV CONPLICITY_OPTIONS=""  
ADD
https://github.com/camptocamp/conplicity/releases/download/${CONPLICITY_VERSION}/conplicity
/bin  
RUN chmod +x /bin/conplicity  
  
COPY run.sh /  
  
CMD [ "sh", "/run.sh" ]

