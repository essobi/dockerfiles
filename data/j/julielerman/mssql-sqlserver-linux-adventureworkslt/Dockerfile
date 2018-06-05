# using vNext image  
FROM microsoft/mssql-server-linux  
  
# set environment variables  
ENV SA_PASSWORD=Passw0rd  
ENV ACCEPT_EULA=Y  
  
COPY entrypoint.sh entrypoint.sh  
COPY SqlCmdStartup.sh SqlCmdStartup.sh  
COPY SqlCmdScript.sql SqlCmdScript.sql  
CMD md SQLServer  
  
COPY AdventureWorksLT.mdf /SQLServer/AdventureWorksLT.mdf  
COPY AdventureWorksLT.ldf /SQLServer/AdventureWorksLT.ldf  
  
# Grant permissions for the SqlCmdStartup.sh script to be executable  
RUN chmod +x ./SqlCmdStartup.sh  
#start everything  
CMD /bin/bash ./entrypoint.sh  

