FROM vmware/powerclicore  
  
ADD backup.ps1 /opt/  
  
VOLUME ["/app"]  
  
CMD ["powershell", "/opt/backup.ps1"]

