FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
unar \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GNUSTEP_STRING_ENCODING UTF-8  
VOLUME /opt/unar  
WORKDIR /opt/unar  
  
ENTRYPOINT ["unar"]  
CMD ["-help"]  

