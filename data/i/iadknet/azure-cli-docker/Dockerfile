FROM microsoft/azure-cli  
  
ENV AZURE_CONFIG_MODE asm  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["azure"]  

