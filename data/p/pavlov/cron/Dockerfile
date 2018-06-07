FROM alpine:latest  
MAINTAINER Alex Kern <alex@usepavlov.com>  
  
RUN wget -O /usr/local/bin/kubectl http://storage.googleapis.com/kubernetes-
release/release/v1.3.6/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
mkdir -p /cron/jobs  
WORKDIR /cron  
COPY cron.sh cron.sh  
  
ENV CRON_INTERVAL "* * * * *"  
CMD [ "sh", "cron.sh" ]  

