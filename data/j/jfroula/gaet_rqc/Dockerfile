FROM debian:jessie  
ENV PROKKA_VERSION v1.12  
ENV BARRNAP_VERSION 212005299c872f71669bbad5858ff97845f5f1d9  
ENV DPRED_VERSION 0.1.0  
ENV GAET_VERSION 0.3.0  
ENV Y2C_VERSION 0.1.0  
ENV DOMAIN_DB /usr/local/domain_db/  
  
ADD image /usr/local/  
  
RUN install.sh && rm -r /usr/local/bin/install.sh /usr/local/bin/install  
  
WORKDIR /root  
ADD image/bin/run.sh /usr/local/bin/run.sh  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/run.sh"]  

