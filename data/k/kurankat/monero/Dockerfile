FROM ubuntu:xenial  
  
ARG BUILD_DATE  
ARG VERSION  
LABEL maintainer="github/kurankat"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /usr/local/monero  
  
RUN apt update && apt -y install wget unzip bzip2 \  
&& wget https://downloads.getmonero.org/linux64 -O monero.tar.bz2 \  
&& tar -vxf monero.tar.bz2 --strip-components=2 \  
&& rm monero.tar.bz2  
  
EXPOSE 18081  
VOLUME /root/.bitmonero  
  
COPY monerod.conf /root/.bitmonero/monerod.conf  
  
ENTRYPOINT ["/usr/local/monero/monerod", "--config-file",
"/root/.bitmonero/monerod.conf", "--non-interactive"]  

