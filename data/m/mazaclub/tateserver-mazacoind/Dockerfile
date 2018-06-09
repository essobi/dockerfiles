FROM mazaclub/mazacoind-base  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
EXPOSE 50001 50002 8000  
VOLUME ["/home/maza","/var/tate-server"]  
ENTRYPOINT ["/sbin/my_init"]  
ENV MAZACOIND localhost  
  
RUN apt-get update \  
&& apt-get install -y \  
apg python-dev python2.7 python-pip \  
git libleveldb1 libleveldb-dev  
  
RUN echo "bitcoin hard nofile 65536" >> /etc/security/limits.conf \  
&& echo "bitcoin soft nofile 65536" >> /etc/security/limits.conf \  
&& cd / \  
&& git clone https://github.com/mazaclub/tate-server /tate-server \  
&& cd /tate-server \  
&& python setup.py install \  
&& mkdir -pv /app \  
&& mv /tate-server/* /app \  
&& rm -rf /etc/service/sshd  
  
ADD . /  
RUN chmod +x /etc/service/tate-server/run  

