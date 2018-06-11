FROM ubuntu:bionic  
MAINTAINER jufab "https://github.com/jufab"  
LABEL authors=jufab  
  
ARG YADOMS_VERSION="2.0.2"  
ENV DEVELOPER_MODE="false"  
RUN apt -qqy update \  
&& apt -qqy install \  
sudo \  
wget \  
&& apt -qyy autoremove \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt -qyy clean  
  
WORKDIR /usr/local/bin  
RUN wget
https://github.com/Yadoms/yadoms/releases/download/${YADOMS_VERSION}/Yadoms-${YADOMS_VERSION}-Linux.tar.gz
\  
&& tar xzvf Yadoms-${YADOMS_VERSION}-Linux.tar.gz \  
&& mv Yadoms-${YADOMS_VERSION}-Linux Yadoms/ \  
&& rm Yadoms-${YADOMS_VERSION}-Linux.tar.gz  
  
ENV PATH /usr/local/bin/Yadoms/bin:$PATH  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["yadoms"]  

