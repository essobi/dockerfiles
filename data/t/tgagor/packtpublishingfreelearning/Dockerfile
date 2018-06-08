FROM alpine:3.5  
MAINTAINER tgagor, https://github.com/tgagor  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
ENV PPFL_EMAIL=youremail \  
PPFL_PASSWORD=yourpassword \  
PPFL_DOWNLOAD_FOLDER=/books \  
PPFL_DOWNLOAD_FORMATS="pdf, epub, mobi, code" \  
PPFL_EXTRAINFOLOGFILEPATH="eBookMetadata.log" \  
PPFL_ANTICAPTCHA_DATA="xxx"  
# run it as unprivileged user  
RUN addgroup -g 1000 ppfl \  
&& adduser -s /bin/sh -u 1000 -G ppfl -D ppfl \  
&& mkdir -p "$PPFL_DOWNLOAD_FOLDER" \  
&& chown -R ppfl:ppfl "$PPFL_DOWNLOAD_FOLDER"  
  
RUN apk --no-cache add python3 git curl \  
&& git clone https://github.com/igbt6/Packt-Publishing-Free-Learning.git
/opt/ppfl \  
&& cd /opt/ppfl \  
&& pip3 install -r requirements.txt \  
&& mv /opt/ppfl/src/* /opt/ppfl \  
&& chown -R ppfl:ppfl /opt/ppfl \  
&& apk del git  
  
COPY run.sh /opt/ppfl/run.sh  
RUN chmod +x /opt/ppfl/run.sh  
  
# USER ppfl  
WORKDIR /opt/ppfl/  
ENTRYPOINT ["/opt/ppfl/run.sh"]  
CMD ["python3", "/opt/ppfl/packtPublishingFreeEbook.py", "-gd"]  

