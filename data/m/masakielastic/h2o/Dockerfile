FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV H2O_VERSION 1.5.0  
RUN apt-get update && apt-get install -y ca-certificates \  
curl build-essential cmake openssl libssl-dev \  
libyaml-dev --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L "https://github.com/h2o/h2o/archive/v$H2O_VERSION.tar.gz" -o
h2o.tar.gz  
RUN tar xfz h2o.tar.gz  
RUN mv "h2o-$H2O_VERSION" /usr/src/h2o  
RUN rm -r h2o.tar.gz  
  
WORKDIR /usr/src/h2o  
RUN cmake . && make h2o  
RUN mv h2o /usr/local/bin  
  
COPY h2o.conf /usr/src/h2o/h2o.conf  
  
RUN mkdir -p /usr/share/h2o/html  
WORKDIR /usr/share/h2o/html  
  
EXPOSE 80 443  
CMD h2o -c /usr/src/h2o/h2o.conf  

