FROM ubuntu:16.04  
MAINTAINER izayoi256 <qwert.izayoi@gmail.com>  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
ca-certificates \  
build-essential \  
libssl-dev \  
libdb++-dev \  
libboost-all-dev \  
libqrencode-dev \  
libminiupnpc-dev \  
tzdata \  
&& cd /tmp \  
&& git clone https://github.com/LoanOrLease/lol.git \  
&& cd lol/src \  
&& mkdir -p obj/zerocoin \  
&& chmod +x ../share/genbuild.sh leveldb/build_detect_platform \  
&& make -f makefile.unix \  
&& chmod +x loanorleased \  
&& mv loanorleased /usr/bin \  
&& apt-get remove -y \  
git \  
ca-certificates \  
build-essential \  
&& apt-get clean \  
&& rm -rf /tmp/*  
  
ADD files /  
RUN chmod +x /usr/local/bin/* \  
&& chmod 600 /root/.loanorlease/loanorlease.conf  
  
ENTRYPOINT ["docker-entrypoint"]  
CMD ["lold-foreground"]  

