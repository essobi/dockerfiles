FROM ubuntu  
MAINTAINER Roy Lines <https://roylines.co.uk>  
  
RUN apt-get install -y wget unzip  
RUN mkdir /etc/nomad.d  
RUN chmod a+w /etc/nomad.d  
  
RUN wget
https://releases.hashicorp.com/nomad/0.1.2/nomad_0.1.2_linux_amd64.zip -O
nomad.zip --no-check-certificate  
RUN unzip nomad.zip  
RUN mv nomad /usr/bin/nomad  
RUN chmod +x /usr/bin/nomad  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
# Expose HTTP API port  
EXPOSE 4646  
CMD ["/usr/bin/entrypoint.sh"]  

