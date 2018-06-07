FROM centurylink/wetty-cli  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
# Install build dependencies  
RUN apt-get -qqy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential autoconf
automake curl groff-base supervisor python-pip screen procps net-tools
bsdutils  
  
RUN chown daemon:daemon /etc/supervisor/conf.d/ /var/run/ /var/log/supervisor/  
  
# Install empserver  
RUN mkdir -p /tmp/empserver /empserver && \  
cd /empserver && \  
curl -Lsq
'https://sourceforge.net/projects/empserver/files/latest/download?source=files'
| tar xz --strip-components 1 && \  
./bootstrap && \  
./configure --prefix=/empserver && \  
make && \  
make install && \  
rm -fr /tmp/empserver  
  
RUN pip install supervisor-stdout  
  
WORKDIR /empserver  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
VOLUME /empserver  
  
# This is what the empire client will connect to  
ENV EMPIREHOST localhost  
ENV EMPIREPORT 6665  
# This is what wetty will listen on  
ENV PORT 3000  
EXPOSE 3000  
EXPOSE 6665  
CMD /run.sh  

