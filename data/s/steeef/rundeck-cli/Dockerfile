FROM openjdk:8  
MAINTAINER Stephen Price <stephen@stp5.net>  
  
ENV DEBIAN_FRONTEND noninteractive \  
RD_URL http://rundeck:4440 \  
RD_TOKEN AFAKETOKENPLEASEREPLACE \  
RD_AUTH_PROMPT false  
  
RUN cd /tmp && \  
curl -Lo /tmp/rundeck-cli.deb https://github.com/rundeck/rundeck-
cli/releases/download/v1.0.5/rundeck-cli_1.0.5-1_all.deb && \  
echo '5ca80483009b4c3ed665fa14f22322231ed9286de20d5475518cfd424e4b5017
rundeck-cli.deb' > /tmp/rundeck-cli.sig && \  
shasum -a256 -c /tmp/rundeck-cli.sig && \  
dpkg -i /tmp/rundeck*.deb && rm /tmp/rundeck*.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/bin/rd"]  
CMD ["--help"]  

