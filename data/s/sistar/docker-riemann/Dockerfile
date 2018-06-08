FROM java:8  
MAINTAINER Matthias Nüßler <m.nuessler@web.de>  
  
ENV RIEMANN_VERSION 0.2.11  
ADD https://aphyr.com/riemann/riemann_${RIEMANN_VERSION}_all.deb /tmp/  
RUN echo "8f074b9ad3321a962d3a32a7a54cf930
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

