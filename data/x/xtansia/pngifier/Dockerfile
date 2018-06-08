FROM xtansia/python35-latex  
MAINTAINER Thomas Farr <xtansia@xtansia.com>  
  
ENV RENDER_TIMEOUT 10s  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
poppler-utils \  
uuid-runtime \  
abcm2ps \  
imagemagick \  
gnuplot \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install aiohttp  
  
ADD latex2png abc2png gnuplot2png pngifier_server /usr/local/bin/  
RUN cd /usr/local/bin && chmod +x latex2png abc2png gnuplot2png
pngifier_server  
  
RUN useradd --system -m -c "pngifier account" -d /pngifier-work -s /bin/false
pngifier  
  
WORKDIR /pngifier-work  
USER pngifier  
CMD /usr/local/bin/pngifier_server  
EXPOSE 8080  

