FROM openjdk:8-jre-slim  
  
LABEL maintainer="Serge Medvedev, s.medvedev@samsung.com"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Riemann  
ENV RIEMANN_VERSION=0.3.1  
RUN wget
https://github.com/riemann/riemann/releases/download/${RIEMANN_VERSION}/riemann-${RIEMANN_VERSION}.tar.bz2
-O - | tar -xj \  
&& cp -lar riemann-${RIEMANN_VERSION}/. / \  
&& sed -ie 's/127.0.0.1/0.0.0.0/' /etc/riemann.config  
  
RUN apt-get remove -y wget \  
&& apt-get autoremove -y  
  
EXPOSE 5555/tcp 5555/udp 5556/tcp  
  
CMD ["riemann", "/etc/riemann.config"]  
  

