FROM ubuntu:14.04  
MAINTAINER Dylan sale <dylan@enabled.com.au>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
mysql-proxy \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
EXPOSE 3306  
EXPOSE 4041  
ENTRYPOINT ["mysql-proxy", "--proxy-address=0.0.0.0:3306" ]  
CMD [ "--help-all" ]  

