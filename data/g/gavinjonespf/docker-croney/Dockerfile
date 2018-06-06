#TODO: Possibly use a generic toolbox image after all?  
#gliderlabs/alpine:3.3 - due to glibc requirements  
FROM frolvlad/alpine-glibc:alpine-3.4  
#Tools  
RUN apk --no-cache add \  
bash \  
ca-certificates \  
nano \  
curl \  
jq  
  
RUN apk --no-cache add \  
python  
RUN apk --no-cache add --virtual build-dependencies \  
python-dev \  
py-pip \  
build-base \  
&& pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz \  
&& apk del build-dependencies  
  
WORKDIR /app  
COPY files/crontab /etc/cron.d/crontab  
RUN touch /var/log/cron.log  
COPY ./scripts scripts  
WORKDIR /app/scripts  
RUN chmod -R +x *.sh  
  
ENTRYPOINT [ "/app/scripts/start.sh" ]  
CMD ["/etc/cron.d/crontab", ""]  

