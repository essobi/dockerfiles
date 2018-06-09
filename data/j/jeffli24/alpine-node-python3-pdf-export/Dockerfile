FROM jeffli24/alpine-node-python3-basic-app-stack:latest  
  
# Download and install wkhtmltopdf  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories; apk upgrade --update-cache --available  
  
RUN apk add --update --no-cache \  
wkhtmltopdf \  
coreutils \  
xvfb \  
dbus && \  
rm -rf /var/cache/apk/* # Delete the cache folder  
  
RUN pip3 install --no-cache-dir \  
beautifulsoup4 \  
pdfkit \  
PyPDF2  
RUN rm -r /root/.cache  
  
# Install xvfb to use wkhtmltopdf without X server  
ADD ./packages/wkhtmltopdf /usr/local/bin/  
ADD ./packages/xvfb-run /usr/bin/  
  
RUN chmod a+x /usr/local/bin/wkhtmltopdf  
RUN chmod +x /usr/bin/xvfb-run

