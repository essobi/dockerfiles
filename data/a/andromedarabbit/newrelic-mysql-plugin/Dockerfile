FROM java:8-jre  
  
MAINTAINER Keaton Choi <keaton@dailyhotel.com>  
  
ENV LICENSE_KEY YOUR_KEY  
ARG INSTALL_SCRIPT_URL=https://download.newrelic.com/npi/release/install-npi-
linux-debian-x64.sh  
  
RUN apt-get update -y && apt-get install -y curl nodejs  
  
RUN UNATTENDED=true bash -c "$(curl ${INSTALL_SCRIPT_URL})"  
  
WORKDIR /  
  
VOLUME ["/data"]  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["./npi", "start", "nrmysql", "--foreground"]  

