FROM mono:4.0.1  
MAINTAINER kcgthb  
  
ENV VERSION 0.6.45.1  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update -q  
RUN apt-get install -qy libcurl4-openssl-dev tar bzip2  
RUN apt-get clean  
RUN curl -L
https://github.com/raspdealer/Jackett/releases/download/v${VERSION}/Jackett.Binaries.Mono.tar.gz
-o /tmp/jackett.tar.gz  
RUN mkdir -p /tmp/jackett  
RUN tar -axvf /tmp/jackett.tar.gz -C /tmp/jackett  
RUN mkdir -p /data/app  
RUN mv /tmp/jackett/*/Jackett/* /data/app  
RUN chown -R nobody:users /data/app  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /data/config  
RUN chown -R nobody:users /data/config  
RUN ln -s /data/config /usr/share/Jackett  
  
EXPOSE 9118  
VOLUME /data/config  
VOLUME /data/app  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
WORKDIR /data/app  
  
ENTRYPOINT ["/start.sh"]  

