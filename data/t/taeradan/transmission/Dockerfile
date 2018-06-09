FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y transmission-daemon  
  
RUN useradd --create-home transmission  
RUN chown transmission:transmission -R /var/lib/transmission-daemon/  
USER transmission  
  
EXPOSE 9091 51413 51413/udp  
  
ENTRYPOINT ["/usr/bin/transmission-daemon"]  
CMD ["-f", "-T", "--allowed", "127.0.0.1"]  

