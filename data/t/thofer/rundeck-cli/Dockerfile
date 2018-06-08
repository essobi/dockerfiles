FROM openjdk:8-jre-slim  
  
MAINTAINER Thomas Ferreira <thomas.ferreira+docker@_n0spam_protonmail.com>  
  
ARG _RD_CLI_VERSION_="1.0.27"  
ARG
_RD_CLI_DEB_CHECKSUM_="636c5b22a6f60d3c9a425895984e43fe9c8b78a3b2b994ca1d89534a75f3dd7154281991041294e557a971837accff311cc8fe1d32e0ba11b2aa4c297bc52af7"  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -Lo /tmp/rundeck-cli.deb https://dl.bintray.com/rundeck/rundeck-
deb/rundeck-cli_${_RD_CLI_VERSION_}-1_all.deb \  
&& echo "${_RD_CLI_DEB_CHECKSUM_} /tmp/rundeck-cli.deb" > /tmp/rundeck-cli.sig
\  
&& sha512sum -c /tmp/rundeck-cli.sig \  
&& dpkg -i /tmp/rundeck*.deb \  
&& rm /tmp/rundeck*.deb /tmp/rundeck-cli.sig\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV RD_AUTH_PROMPT false  
  
ENTRYPOINT ["/usr/bin/rd"]  
CMD ["--help"]  

