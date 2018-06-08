FROM lucidprogrammer/python3-tesseract4-base:latest as base  
LABEL maintainer="Lucid Programmer"  
RUN apt-get update && apt-get install -y \  
wget  
# https://github.com/prasmussen/gdrive #  
RUN wget -O gdrive https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA  
  
FROM lucidprogrammer/python3-tesseract4-base:latest  
COPY \--from=base /work/gdrive /usr/local/bin  
RUN chmod +x /usr/local/bin/gdrive  
  
RUN apt-get update && apt-get install -y git ca-certificates poppler-utils
pdftk && \  
rm -rf /var/lib/apt/lists/*  

