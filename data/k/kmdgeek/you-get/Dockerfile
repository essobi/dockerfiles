FROM python:3-alpine  
LABEL maintainer="kmdgeek"  
  
RUN apk --no-cache add build-base ffmpeg mpv \  
&& pip3 install --no-cache-dir ykdl \  
&& apk del build-base \  
&& mkdir -p /download  
  
WORKDIR /download  
  
ENTRYPOINT [ "ykdl" ]  
CMD [ "--help" ]  

