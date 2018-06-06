FROM python:2.7  
MAINTAINER Eric Vallee (eric_vallee@webificservices.com)  
  
ENV UID="1000"  
RUN echo "letsencrypt-client:x:${UID}:${UID}:letsencrypt-
client,,,:/home/letsencrypt-client:/bin/bash" >> /etc/passwd  
RUN echo "letsencrypt-client:x:${UID}:" >> /etc/group  
RUN mkdir /home/letsencrypt-client  
  
ADD https://raw.githubusercontent.com/diafygi/acme-tiny/master/acme_tiny.py
/opt/acme_tiny.py  
COPY ["./run.sh", "/opt/run.sh"]  
  
RUN chown ${UID}:${UID} /opt/run.sh && \  
chown ${UID}:${UID} /opt/acme_tiny.py && \  
mkdir -p /etc/letsencrypt/live && \  
chown -R ${UID}:${UID} /etc/letsencrypt/live && \  
mkdir -p /home/node-app/challenge && \  
chown -R ${UID}:${UID} /home/node-app/challenge && \  
chown -R ${UID}:${UID} /home/letsencrypt-client  
  
USER $UID  
ENTRYPOINT [ "bash" ]  
CMD [ "/opt/run.sh" ]  

