FROM debian:stable-slim  
  
# Set to Non-Interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install all TeX and LaTeX dependences  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends \  
texlive \  
texlive-latex-extra \  
pandoc && \  
apt-get autoclean && \  
apt-get --purge --yes autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Export the output data  
WORKDIR /data  
VOLUME ["/data"]  
  
ENTRYPOINT ["pandoc"]  
  
CMD ["--help"]  

