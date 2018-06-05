FROM scf37/base:latest  
  
RUN curl https://get.acme.sh | sh && \  
/root/.acme.sh/acme.sh --uninstallcronjob && \  
apt-get -y update && apt-get -y install docker.io && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
COPY run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]

