FROM openjdk:8  
ENV RIEMANN_VERSION 0.2.14  
RUN curl -s -L -O
https://github.com/riemann/riemann/releases/download/${RIEMANN_VERSION}/riemann-${RIEMANN_VERSION}.tar.bz2
&& \  
tar xvjf riemann-${RIEMANN_VERSION}.tar.bz2 && \  
cp -r riemann-${RIEMANN_VERSION}/* /usr/local/ && \  
rm -rf riemann-${RIEMANN_VERSION}* /usr/local/etc/riemann.config && \  
mkdir -p /usr/local/etc/riemann  
  
COPY /etc/ /usr/local/etc/riemann/  
  
EXPOSE 5555/tcp 5555/udp 5556/tcp  
  
CMD ["/usr/local/bin/riemann", "/usr/local/etc/riemann/riemann.config"]  

