FROM debian:jessie  
MAINTAINER Oliver Soell <oliver@soell.net>  
  
ENV COPERNICUS_VERSION 2.1.4  
ENV COPERNICUS_PASSWORD default  
  
RUN apt-get update -y &&\  
apt-get install -y python ca-certificates curl build-essential --no-install-
recommends &&\  
curl -sL
https://github.com/gromacs/copernicus/archive/${COPERNICUS_VERSION}.tar.gz |
tar zxfv - -C /var/tmp &&\  
mv /var/tmp/copernicus-${COPERNICUS_VERSION} /opt/copernicus &&\  
apt-get install -y python-dev cython &&\  
cd /opt/copernicus &&\  
find ./ -type f -exec sed -i -e 's/ssl.PROTOCOL_SSLv3/ssl.PROTOCOL_SSLv23/g'
{} \; &&\  
./compileLibraries.sh &&\  
rm -rf /opt/copernicus/test &&\  
apt-get remove -y curl python-dev build-essential &&\  
apt-get autoremove -y &&\  
rm -rf /var/lib/apt/lists  
  
RUN useradd -m -u 1000 copernicus  
RUN chown -R 1000:1000 /home/copernicus  
USER copernicus  
WORKDIR /home/copernicus  
ENV PATH $PATH:/opt/copernicus:/opt/gromacs/bin  
  
EXPOSE 13807 14807  
VOLUME /home/copernicus  
  
ADD server-init.sh /server-init.sh  
CMD ["/server-init.sh", "cpc-server", "start", "-dev"]  

