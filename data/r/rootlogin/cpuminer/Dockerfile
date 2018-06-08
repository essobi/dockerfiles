FROM debian:9  
MAINTAINER Simon Erhardt <me+docker@rootlogin.ch>  
  
ENV TINI_VERSION=v0.15.0 \  
WALLET=47a9xZBTpijUgmGWQXQqyM7V4bvcksTu8WZuW1G87Woh6uPaBQzbAg9Pn4LCV4Be7sMRNCRVcEk6SEFkiVPibGxnKEZeY35
\  
THREADS=2 \  
WORKER=x  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
ADD docker-run.sh /docker-run.sh  
  
RUN apt-get update \  
&& apt-get install -y \  
automake \  
build-essential \  
ca-certificates \  
curl \  
git \  
libcurl4-openssl-dev \  
libssl1.0-dev \  
&& apt-get autoclean \  
&& chmod +x /usr/local/bin/tini /docker-run.sh \  
&& cd /opt \  
&& git clone https://github.com/OhGodAPet/cpuminer-multi.git \  
&& cd cpuminer-multi \  
&& ./autogen.sh \  
&& CFLAGS="-march=native" ./configure \  
&& make \  
&& make install  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
CMD /docker-run.sh  

