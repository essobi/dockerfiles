FROM ubuntu  
RUN apt-get update \  
&& apt-get install -y curl default-jre-headless  
RUN curl -O -L http://aphyr.com/riemann/riemann_0.2.10_all.deb \  
&& dpkg -i riemann*deb && rm -f riemann*deb  
EXPOSE 5555  
EXPOSE 5555/udp  
EXPOSE 5556  
# Share the config directory as a volume  
VOLUME /etc/riemann  
ADD riemann.config /etc/riemann/riemann.config  
# Set the hostname in /etc/hosts so that Riemann doesn't die due to
unknownHostException  
CMD echo 127.0.0.1 $(hostname) > /etc/hosts; /usr/bin/riemann
/etc/riemann/riemann.config  

