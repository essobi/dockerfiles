FROM debian:stretch-slim  
LABEL maintainer="Mattia Monga <mattia.monga@unimi.it>"  
ENV DEBIAN_FRONTEND noninteractive  
USER root  
# workaround slim image  
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7  
RUN apt-get update && apt-get install -yq ghostscript libreoffice psmisc
unoconv wkhtmltopdf && apt-get clean && rm -rf /var/lib/apt/*  
RUN useradd user  
USER user  
COPY mkpdf.sh /usr/local/bin/mkpdf.sh  
WORKDIR /home/user  
# ENV needed since no xserver is present (see wkhtmltopdf README.Debian)  
ENV QT_QPA_FONTDIR /usr/share/fonts/truetype/dejavu/  
ENV QT_QPA_PLATFORM offscreen  
CMD ["/bin/bash", "-c", "/usr/local/bin/mkpdf.sh"]  

