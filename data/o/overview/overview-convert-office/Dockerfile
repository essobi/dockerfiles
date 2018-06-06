FROM alpine:3.7 AS os  
RUN set -x \  
&& apk add --update --no-cache \  
jq \  
libreoffice \  
ttf-freefont \  
msttcorefonts-installer \  
tini \  
&& update-ms-fonts \  
&& fc-cache -f  
WORKDIR /app  
  
FROM overview/overview-convert-framework:0.0.15 AS framework  
# multi-stage build  
FROM os AS base  
WORKDIR /app  
COPY \--from=framework /app/run /app/run  
COPY \--from=framework /app/convert-single-file /app/convert  
COPY ./do-convert-single-file /app/do-convert-single-file  
CMD [ "tini", "--", "/app/run" ]  
  
FROM base AS test  
COPY \--from=framework /app/test-convert-single-file /app/  
COPY test/ /app/test/  
ENV TIMEOUT 5  
RUN [ "/app/test-convert-single-file" ]  
CMD [ "true" ]  
  
FROM base AS production  

