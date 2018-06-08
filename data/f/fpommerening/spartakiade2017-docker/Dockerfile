FROM mono:4.6.1  
MAINTAINER Frank Pommerening "frank@pommerening-online.de"  
ENV REFRESHED_AT 2017-03-02  
ENV StartupApp_VERSION 0.0.2  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget p7zip && rm -rf /var/lib/apt/lists/* \  
&& wget -O /home/StartupApp.7z
"https://github.com/fpommerening/Spartakiade2017-Docker/releases/download/$StartupApp_VERSION/StartupApp.7z"
\  
&& p7zip -d /home/StartupApp.7z \  
&& mv /StartupApp/ /app/ \  
&& apt-get purge -y --auto-remove ca-certificates wget p7zip  
  
WORKDIR /app/  
EXPOSE 18317  
ENTRYPOINT ["mono", "StartupApp.exe"]

