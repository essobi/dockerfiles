FROM ubuntu:artful  
  
RUN apt-get update && \  
apt-get install -y wget perl build-essential libssl-dev libnet-ssleay-perl
libcrypt-ssleay-perl libidn11-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PERL_MM_USE_DEFAULT 1  
RUN cpan CPAN && \  
cpan Net::DNS && \  
cpan Net::SSLeay && \  
cpan IO::Socket::SSL && \  
cpan IO::Socket::INET  
  
ENV DOWNLOAD_URL https://github.com/OWASP/O-Saft/archive/17.07.17.tar.gz  
ENV DOWNLOAD_CHECKSUM
84a448c4aeb83b90a4888025f7e04f19470d122f5b1229ad54136709344c0531  
ENV DOWNLOAD_LOCATION /opt/osaft.tar.gz  
ENV CHECKSUM_LOCATION /osaft-checksum  
  
RUN wget $DOWNLOAD_URL -O $DOWNLOAD_LOCATION && \  
echo "$DOWNLOAD_CHECKSUM $DOWNLOAD_LOCATION" > $CHECKSUM_LOCATION && \  
sha256sum --check $CHECKSUM_LOCATION && \  
cd /opt && tar -xzf $DOWNLOAD_LOCATION && \  
rm -f $DOWNLOAD_LOCATION && \  
mv /opt/* /opt/osaft  
  
WORKDIR /opt/osaft  
  
ENTRYPOINT ["perl", "/opt/osaft/o-saft.pl"]  

