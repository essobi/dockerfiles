FROM microsoft/dotnet:2.0-runtime-jessie  
  
EXPOSE 11015  
RUN apt-get -y update && apt-get clean  
RUN apt-get install --no-install-recommends -y \  
wget  
  
CMD mkdir /opt/Ombi  
WORKDIR /opt/Ombi  
RUN wget
https://ci.appveyor.com/api/buildjobs/jqegwte5rpdg49ed/artifacts/linux.tar.gz  
RUN tar xzf linux.tar.gz  
CMD chmod +x Ombi  
COPY ./docker-entrypoint.sh /opt/  
RUN chmod +x /opt/docker-entrypoint.sh  
  
EXPOSE 5000  
ENTRYPOINT ["/opt/docker-entrypoint.sh"]

