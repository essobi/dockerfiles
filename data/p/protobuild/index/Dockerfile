FROM microsoft/dotnet:1.1-sdk-msbuild  
  
RUN apt-get update  
RUN apt-get install -y nginx nodejs npm git supervisor dos2unix  
RUN npm install -g bower  
  
ADD src /srv/protobuild/src  
WORKDIR /srv/protobuild/src/Protobuild.Website  
RUN dotnet restore  
  
RUN dotnet publish -c Release -o /srv/protobuild/pkg ./  
  
ADD extra/nginx /srv/nginx  
ADD extra/run.sh /srv/extra/run.sh  
ADD extra/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir -pv /var/log/nginx /var/log/supervisor  
  
RUN dos2unix /srv/extra/run.sh  
RUN chmod a+X /srv/extra/run.sh  
  
ENV ASPNETCORE_ENVIRONMENT Production  
ENV ASPNETCORE_URLS http://*:5000  
ENV DOMAIN http://localhost:8080  
ENV GOOGLE_PROJECT_ID protobuild-index  
ENV GOOGLE_SERVICE_ACCOUNT_JSON_PATH Credentials/ServiceAccount.json  
ENV GOOGLE_OAUTH_CLIENT_JSON_PATH Credentials/OAuthClient.json  
  
WORKDIR /srv/protobuild/pkg  
ENTRYPOINT ["/usr/bin/supervisord", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  

