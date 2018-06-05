FROM blacksquare/ruby:2.4  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libsqlite3-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install mailcatcher --no-rdoc --no-ri  
  
ENV SMTP_PORT=1025 \  
HTTP_PORT=1080  
EXPOSE ${SMTP_PORT} ${HTTP_PORT}  
  
CMD mailcatcher --smtp-ip=0.0.0.0 --smtp-port=$SMTP_PORT \--http-ip=0.0.0.0
--http-port=$HTTP_PORT -f  

