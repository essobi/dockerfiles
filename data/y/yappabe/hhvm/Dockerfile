FROM debian:jessie  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 && \  
echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes hhvm-dbg  
  
EXPOSE 9000  
COPY run.sh /run.sh  
COPY php.ini /etc/hhvm/php.ini  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]

