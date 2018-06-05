FROM microsoft/aspnet:1.0.0-rc1-update1  
  
COPY project.json /tmp/  
WORKDIR /tmp  
RUN dnu restore  
WORKDIR /  
  
ENV DNX_VERSION=1.0.0-rc1-final DNX_USER_HOME=/opt/dnx  
RUN dnu commands install Microsoft.Dnx.Watcher $DNX_VERSION \--packages
$DNX_USER_HOME/bin  
  
VOLUME /project  
  
COPY rundnx.sh /  
  
EXPOSE 5000/tcp  
  
CMD ["/bin/bash", "/rundnx.sh"]  

