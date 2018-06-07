FROM m13253/doh-infrastructure:common  
  
RUN mkdir /opt && \  
git clone https://github.com/m13253/dns-over-https.git /opt/dns-over-https &&
\  
cd /opt/dns-over-https && \  
make  
  
COPY unbound.conf /usr/local/etc/unbound/unbound.conf  
COPY doh-*.conf /etc/dns-over-https/  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 8054  
CMD /entrypoint.sh  

