FROM buildpack-deps:jessie-curl  
MAINTAINER Hans Kristian Flaatten <hans@starefossen.com>  
  
ENV TRANSPORTER_VERSION 0.1.1  
ENV TRANSPORTER_TAG v${TRANSPORTER_VERSION}  
  
RUN curl --verbose -SLO
"https://github.com/compose/transporter/releases/download/${TRANSPORTER_TAG}/transporter_linux_amd64.tar.gz"
\  
&& tar -xzf "transporter_linux_amd64.tar.gz" -C /usr/local/bin --strip-
components=1 \  
&& rm "transporter_linux_amd64.tar.gz"  
  
ENTRYPOINT [ "transporter" ]  

