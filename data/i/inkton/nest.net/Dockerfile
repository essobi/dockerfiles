FROM microsoft/aspnetcore-build:2.0.0-jessie  
  
MAINTAINER nest.yt  
  
ENV ASPNETCORE_ENVIRONMENT Development  
ENV NUGET_XMLDOC_MODE skip  
  
ADD run.sh /run.sh  
  
RUN apt-get update && \  
apt-get install -y vim jq python-pip python-dev mariadb-client sudo unzip
rsync dropbear && \  
rm /etc/dropbear/dropbear_dss_host_key /etc/dropbear/dropbear_rsa_host_key &&
\  
curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v latest -l /vsdbg && \  
git clone https://github.com/inkton/nester.cli.git /usr/local/nester && \  
chmod +x /run.sh && \  
cd /usr/local/nester && make install  
  
WORKDIR "/var/app"  
  
EXPOSE 22  
CMD ["/run.sh"]  

