FROM ubuntu  
  
  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
socat \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["socat"]  
CMD ["-h"]  

