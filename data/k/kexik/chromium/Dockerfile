FROM alpine:latest  
  
RUN apk add \--no-cache udev font-adobe-100dpi font-noto chromium  
RUN delgroup audio && \  
addgroup -g 92 audio && \  
adduser -D chromium -u 1111 -G audio chromium  
  
ENV DISPLAY :0  
USER chromium  
  
CMD chromium-browser --no-sandbox  

