FROM alpine  
  
COPY theme.*.json /  
  
RUN mkdir -p /themes  
  
ENTRYPOINT ["cp", "-v", "/theme.*.json", "/themes/"]  

