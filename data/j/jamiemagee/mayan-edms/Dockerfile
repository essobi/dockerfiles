FROM python:2.7  
MAINTAINER Jamie Magee "jamie.magee@gmail.com"  
# Install base libraries  
RUN apt-get update && \  
apt-get install -y -q --no-install-recommends \  
sudo \  
netcat-openbsd \  
python-dev \  
python-pip \  
nginx \  
libpq-dev \  
git-core \  
libjpeg-dev \  
libmagic1 \  
libpng-dev \  
libreoffice \  
libtiff-dev \  
gcc \  
ghostscript \  
gpgv \  
tesseract-ocr \  
unpaper \  
poppler-utils && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /var/cache/apt/archives/*.deb  
  
# Clone and install mayan edms  
ENV MAYAN_VERSION v2.7.3  
RUN mkdir -p /usr/src/mayan && \  
git clone https://gitlab.com/mayan-edms/mayan-edms.git /usr/src/mayan && \  
(cd /usr/src/mayan && git checkout -q tags/$MAYAN_VERSION) && \  
(cd /usr/src/mayan && pip install --no-cache-dir -r requirements.txt)  
  
# Create directories  
RUN mkdir -p /usr/src/mayan/mayan/media/document_cache  
RUN mkdir -p /usr/src/mayan/mayan/media/document_storage  
  
# Set working dir  
WORKDIR /usr/src/mayan  
  
# Create user  
RUN groupadd -g 1000 mayan \  
&& useradd -u 1000 -g 1000 -d /usr/src/mayan mayan \  
&& chown -Rh mayan:mayan /usr/src/mayan  
  
# Setup entrypoint  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
# Mount volume  
VOLUME ["/usr/src/mayan/mayan/media", "/tmp/settings.conf"]  
EXPOSE 8000  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["runserver", "--insecure", "0.0.0.0:8000"]  

