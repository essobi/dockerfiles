FROM debian:stretch  
  
RUN apt-get update && apt-get install -y \  
gnuradio \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "gnuradio-companion" ]  

