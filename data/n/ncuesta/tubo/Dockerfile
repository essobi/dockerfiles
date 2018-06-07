FROM alpine:latest AS caas  
ARG
CMDAS_URL="https://github.com/chrodriguez/cmd_as_service/archive/1.0.0.tar.gz"  
RUN mkdir -p /tmp/cmd && \  
wget -qO app.tgz "$CMDAS_URL" && \  
tar -xzf app.tgz -C /tmp/cmd --strip-components=1  
  
FROM ruby:2.4-alpine  
LABEL maintainer="Desarrollo CeSPI <desarrollo@cespi.unlp.edu.ar>"  
  
ENV RACK_ENV=production \  
CMD_AS=/bin/tubo  
  
WORKDIR /cmd_as_service  
COPY \--from=caas /tmp/cmd /cmd_as_service  
RUN apk add -U --no-cache bash build-base curl gzip mariadb-client && \  
bundle --frozen  
COPY ./bin/tubo.sh /bin/tubo  
  
CMD ["puma", "-w", "1", "-t", "2:4"]  

