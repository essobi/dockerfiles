FROM google/cloud-sdk:198.0.0  
ENV CLOUDSDK_PYTHON_SITEPACKAGES=1  
RUN apt-get update \  
&& apt-get install -y \  
postgresql-client\  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY bigquery-upload.sh /usr/local/bin  
  
CMD [ "/usr/bin/bq", "ls" ]

