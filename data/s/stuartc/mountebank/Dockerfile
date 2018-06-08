FROM ubuntu  
  
MAINTAINER Stuart Clark "stuart.clark@Jahingo.com"  
  
RUN apt-get update && apt-get install -y curl ca-certificates --no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& curl -SL
"https://s3.amazonaws.com/mountebank/v1.2/mountebank_1.2.30_amd64.deb" -o
mountebank.deb \  
&& dpkg --install mountebank.deb \  
&& rm mountebank.deb \  
&& apt-get purge -y \--auto-remove curl  
  
EXPOSE 2525  
  
CMD ["mb"]  

