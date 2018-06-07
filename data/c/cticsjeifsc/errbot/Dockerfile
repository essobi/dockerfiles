FROM python:3.6  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL maintainer="boidacarapreta@gmail.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="CTIC-SJE-IFSC Kubernetes: Errbot chatbot" \  
org.label-schema.description="Nuvem privada do Câmpus São José do IFSC" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://projetos.sj.ifsc.edu.br" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ctic-sje-
ifsc/servicos_kubernetes" \  
org.label-schema.vendor="CTIC" \  
org.label-schema.version="5.1.2" \  
org.label-schema.schema-version="1.0"  
  
COPY ./docker-entrypoint.sh /  
COPY ./requirements.txt /  
RUN chmod 0755 /docker-entrypoint.sh && \  
pip install -r /requirements.txt && \  
groupadd errbot && \  
useradd -g errbot -d /errbot -m -s /bin/false errbot && \  
errbot --init /errbot && \  
chown -R errbot:errbot /errbot && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/errbot"]  
WORKDIR "/errbot"  
USER "errbot"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/local/bin/errbot"]  

