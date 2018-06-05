FROM microsoft/aspnet:1.0.0-rc1-update1-coreclr  
  
COPY project.json /tmp/  
  
WORKDIR /tmp  
  
RUN dnu restore  
RUN rm /tmp/project.json /tmp/project.lock.json  
  
WORKDIR /

