FROM debian:jessie-slim  
LABEL creator="Johannes Schickling <schickling.j@gmail.com>"  
LABEL maintainer="Alex Knol <alexknol@gmail.com>"  
  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ENV POSTGRES_DATABASE **None**  
ENV POSTGRES_HOST **None**  
ENV POSTGRES_PORT 5432  
ENV POSTGRES_USER **None**  
ENV POSTGRES_PASSWORD **None**  
ENV POSTGRES_EXTRA_OPTS ''  
ENV AZURE_TENANT_ID **None**  
ENV AZURE_APP_ID **None**  
ENV AZURE_SECRET_ID **None**  
ENV AZURE_STORAGE_ACCOUNT **None**  
ENV AZURE_STORAGE_ACCESS_KEY **None**  
ENV AZURE_STORAGE_CONTAINER **None**  
ENV AZURE_BLOB_NAME **None**  
  
ENV SCHEDULE **None**  
  
ADD run.sh run.sh  
ADD backup.sh backup.sh  
ADD restore.sh restore.sh  
  
CMD ["sh", "run.sh"]  

