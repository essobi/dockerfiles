#  
# Riemann server  
#  
# Version 0.2.10  
#  
FROM huahaiy/oracle-java  
  
MAINTAINER Huahai Yang <hyang@juji-inc.com>  
  
RUN \  
echo "===> install Riemann..." && \  
wget https://aphyr.com/riemann/riemann_0.2.10_all.deb && \  
dpkg -i riemann_0.2.10_all.deb && \  
rm riemann_0.2.10_all.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ./docker-entrypoint.sh /  
  
ENV RIEMANN_CONFIG_INCLUDE_DIR /riemann  
  
VOLUME ["/riemann", "/var/log/riemann"]  
  
EXPOSE 5555 5555/udp 5556  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["riemann"]  

