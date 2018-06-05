FROM microsoft/azure-cli:0.10.1  
ENV AZURE_STORAGE_ACCOUNT=test \  
AZURE_STORAGE_ACCESS_KEY=secret \  
AZURE_STORAGE_CONTAINER=test \  
MTIME_THRESHOLD=30 \  
DRY_RUN=true  
  
COPY filter_old_files.py /  
COPY entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
  
CMD /entrypoint.sh  

