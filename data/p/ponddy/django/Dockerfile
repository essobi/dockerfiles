FROM alpine:3.7  
# Change working directory  
WORKDIR /usr/src/app  
  
# Volumes  
VOLUME /usr/src/app/log  
VOLUME /usr/src/app/media  
VOLUME /usr/src/app/assets  
  
# Posts  
EXPOSE 8000  
# Install packages  
RUN apk add --no-cache \  
python3 \  
python3-dev \  
linux-headers \  
gcc \  
musl-dev \  
mariadb-dev  
  
# Copy docker-entrypoint.sh  
COPY ./docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# Update all packages  
ONBUILD RUN apk upgrade --no-cache  
  
# Update pip and setuptools  
ONBUILD RUN pip3 install --upgrade --no-cache-dir pip setuptools uwsgi  
  
# Copy Djnago project to working directory  
ONBUILD COPY . .  
  
# Run!  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]  

