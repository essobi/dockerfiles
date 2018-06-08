FROM openjdk:8-jre-slim  
  
ENV RIEMANN_VERSION 0.3.0  
ADD
https://github.com/riemann/riemann/releases/download/${RIEMANN_VERSION}/riemann_${RIEMANN_VERSION}_all.deb
/tmp/  
RUN echo "f4de4bbe70b8ce4c9ec3a6174cda1f2b
/tmp/riemann_${RIEMANN_VERSION}_all.deb" \  
> /tmp/riemann_${RIEMANN_VERSION}.md5 && \  
md5sum -c /tmp/riemann_${RIEMANN_VERSION}.md5 && \  
dpkg -i /tmp/riemann_${RIEMANN_VERSION}_all.deb && \  
rm /tmp/riemann* && \  
mkdir -p /etc/riemann/config  
  
COPY riemann.config /etc/riemann/riemann.config  
COPY default.config /etc/riemann/config/99-default.config  
COPY riemann.sh /riemann.sh  
  
EXPOSE 5555  
EXPOSE 5556  
ENTRYPOINT ["/riemann.sh"]  

