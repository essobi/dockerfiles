FROM ubuntu:xenial  
  
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
  
ENV DOWNLOAD_URL https://github.com/OWASP/O-Saft/archive/17.04.17.tar.gz  
ENV DOWNLOAD_CHECKSUM
6a997f7eafbb986cc451e39357d12cd24afa3b745887d417e90147a0d051af87  
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

