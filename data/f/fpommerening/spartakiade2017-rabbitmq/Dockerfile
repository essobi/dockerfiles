FROM microsoft/dotnet:1.0.3-core  
MAINTAINER Frank Pommerening "frank@pommerening-online.de"  
ENV REFRESHED_AT 2017-01-25  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget p7zip && rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove  

