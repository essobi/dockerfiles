FROM alpine:3.7  
MAINTAINER Martin Elsner <martin.elsner@gmail.com>  
  
RUN apk update && apk --no-cache add \  
fontconfig \  
libreoffice \  
msttcorefonts-installer \  
ttf-droid-nonlatin \  
ttf-droid \  
ttf-dejavu \  
ttf-freefont \  
ttf-liberation  
  
RUN update-ms-fonts  
RUN fc-cache -f  
RUN pip3 install unoconv  
  
# LibreOffice needs write access to the current users home directory to create
some temporary files.  
# We can convince LibreOffice that this users home directory is somewhere else
by setting the HOME environment variable:  
ENV HOME=/tmp  
# Then we can mount a tmpfs where LibreOffice writes its temporary files:  
VOLUME /tmp  
  
EXPOSE 2002  
ENTRYPOINT ["/usr/bin/unoconv", "--listener", "-vv", "--server", "0.0.0.0"]  

