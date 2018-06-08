FROM microsoft/nanoserver  
  
LABEL maintainer "Andy Clarke"  
  
ENV PORT 2525  
ADD https://s3.amazonaws.com/mountebank/v1.11/mountebank-v1.11.0-win-x64.zip /  
  
RUN powershell -command Expand-Archive -Path mountebank-v1.11.0-win-x64.zip
-DestinationPath /  
  
WORKDIR mountebank-v1.11.0-win-x64  
  
EXPOSE $PORT  
  
CMD mb.cmd --port %PORT%  

