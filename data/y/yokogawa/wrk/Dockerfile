FROM debian:latest  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN apt-get update \  
&& apt-get --no-install-recommends -y install \  
curl \  
ca-certificates \  
make \  
gcc \  
libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
ENV WRK_VERSION 4.0.1  
RUN curl -L https://github.com/wg/wrk/archive/${WRK_VERSION}.tar.gz | tar xzf
- \  
&& ln -snvf /wrk-${WRK_VERSION} /wrk \  
&& cd /wrk \  
&& make  
  
ENTRYPOINT ["/wrk/wrk"]  
CMD ["--help"]  

