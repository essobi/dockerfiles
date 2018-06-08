FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y liquidsoap \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y \  
&& apt-get autoremove -y  
  
RUN chown -R liquidsoap:liquidsoap /home/  
COPY config/radio.liq /home/liquidsoap/config/radio.liq  
WORKDIR /home/liquidsoap  
USER liquidsoap  
CMD ["liquidsoap", "-v", "/home/liquidsoap/config/radio.liq"]

