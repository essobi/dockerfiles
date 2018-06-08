FROM travix/base-debian-jre8:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV RIEMANN_VERSION=0.2.10  
# install riemann  
RUN curl -fSL "https://aphyr.com/riemann/riemann_${RIEMANN_VERSION}_all.deb"
-o riemann.deb \  
&& dpkg -i riemann.deb \  
&& rm -rf riemann.deb \  
&& sed -i -e "s/127.0.0.1/0.0.0.0/" /etc/riemann/riemann.config  
  
# expose ports  
EXPOSE 5555 5556 16384  
# define default command  
CMD /usr/bin/riemann /etc/riemann/riemann.config

