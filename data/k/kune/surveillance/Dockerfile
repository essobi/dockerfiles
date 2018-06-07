FROM alpine:latest  
RUN apk update && apk add bash wget imagemagick msttcorefonts-installer ffmpeg
&& rm -Rf /var/cache/apk/*  
RUN update-ms-fonts && fc-cache -f  
COPY survey.sh /survey.sh  
COPY convert.sh /convert.sh  
COPY index.html /index.html  
RUN chmod +x /survey.sh /convert.sh  
ENTRYPOINT bash -c "/survey.sh"  

