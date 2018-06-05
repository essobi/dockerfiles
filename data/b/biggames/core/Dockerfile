FROM microsoft/dotnet:2.0.6-runtime  
  
LABEL Author="!Dark!, <dark@biggames.pl>"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends openssl curl bzip2 sqlite && \  
adduser -D -h /home/container container  
  
RUN mkdir /dotnetapp && cd /dotnetapp && \  
curl -o PTD.Api.tar.bz2 https://dl.biggames.pl/dl/PayTipDonate/PTD.Api.tar.bz2
&& \  
tar -xjf ./PTD.Api.tar.bz2 && rm PTD.Api.tar.bz2  
  
RUN apt-get remove -y bzip2  
  
USER container  
ENV USER=container HOME=/home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

