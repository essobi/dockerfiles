FROM mtneug/liquidsoap  
  
USER root  
  
RUN mkdir -p /home/liquidsoap/radio  
  
COPY radio /home/liquidsoap/radio  
  
USER liquidsoap  
  
CMD ["liquidsoap", "/home/liquidsoap/radio/myscript.liq"]  

