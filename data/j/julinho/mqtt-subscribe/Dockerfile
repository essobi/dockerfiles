FROM python:3.6  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL maintainer="thia.mdossantos@gmail.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Julinho IFSC: mqtt-subscribe" \  
org.label-schema.description="Script para receber dados do mqtt" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://marvietech.com.br/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/julinho-ifsc/mqtt-subscribe" \  
org.label-schema.vendor="Marvi•E Technologies" \  
org.label-schema.version="3.6" \  
org.label-schema.schema-version="1.0"  
  
COPY docker-entrypoint.sh requirements.txt main.py /  
RUN chmod 0755 /docker-entrypoint.sh && \  
pip install --no-cache-dir -r requirements.txt && \  
groupadd mqtt-subscribe && \  
useradd -g mqtt-subscribe -d /mqtt-subscribe -m -s /bin/false mqtt-subscribe
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/"  
USER "mqtt-subscribe"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["python", "main.py"]  

