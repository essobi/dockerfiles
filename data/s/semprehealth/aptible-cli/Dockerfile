FROM debian:8.8  
COPY ssh_config /etc/ssh/ssh_config  
  
# Found at: https://www.aptible.com/support/toolbelt/#download-debian  
ENV URL "https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-
aptible-toolbelt/master/168/pkg/aptible-
toolbelt_0.15.2%2B20171208092232%7Edebian.8.6-1_amd64.deb"  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -o aptible-cli.deb "$URL" \  
&& dpkg -i aptible-cli.deb \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f aptible-cli.deb  
  
ENTRYPOINT ["aptible"]  
CMD ["help"]  

