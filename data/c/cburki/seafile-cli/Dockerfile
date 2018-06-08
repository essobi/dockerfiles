FROM debian:jessie  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
ENV SEAFILE_CLI_VERSION latest  
  
# Install system requirements  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
locales \  
python && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Configure locales and timezone  
RUN locale-gen en_GB.UTF-8 fr_CH.UTF-8 en_US.UTF-8 && \  
cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime && \  
echo "Europe/Zurich" > /etc/timezone  
  
# Install seafile cli  
ADD https://download.seafile.de/seafile-
cli_${SEAFILE_CLI_VERSION}_x86-64.tar.gz /tmp/seafile-cli.tar.gz  
RUN tar zxvf /tmp/seafile-cli.tar.gz -C /opt/ && \  
ln -s /opt/seafile-cli-${SEAFILE_CLI_VERSION}/seaf-cli /usr/local/bin/  
  
# s6 install and config  
COPY bin/* /usr/bin/  
COPY configs/etc/s6 /etc/s6/  
RUN chmod a+x /usr/bin/s6-* && \  
chmod a+x /etc/s6/.s6-svscan/finish /etc/s6/seafile-cli/finish
/etc/s6/seafile-cli/run  
  
# install scripts  
COPY scripts/setup.sh /opt/setup.sh  
RUN chmod a+x /opt/setup.sh  
  
CMD ["/usr/bin/s6-svscan", "/etc/s6"]  

