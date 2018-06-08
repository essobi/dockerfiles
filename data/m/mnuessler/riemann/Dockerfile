FROM openjdk:8-jre-slim  
  
MAINTAINER Matthias Nüßler <m.nuessler@web.de>  
  
ENV RIEMANN_VERSION 0.2.14  
ADD
https://github.com/riemann/riemann/releases/download/${RIEMANN_VERSION}/riemann_${RIEMANN_VERSION}_all.deb
/tmp/  
RUN echo "5a60d6eebb2fd9a8603397386476006e
/tmp/riemann_${RIEMANN_VERSION}_all.deb" \  
> /tmp/riemann_${RIEMANN_VERSION}.md5 && \  
md5sum -c /tmp/riemann_${RIEMANN_VERSION}.md5 && \  
dpkg -i /tmp/riemann_${RIEMANN_VERSION}_all.deb && \  
rm /tmp/riemann* && \  
mkdir -p /etc/riemann/conf.d  
  
COPY riemann.config /etc/riemann/  
  
EXPOSE 5555 5556  
CMD ["start"]  
ENTRYPOINT ["/usr/bin/riemann"]  

