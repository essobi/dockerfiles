FROM python:2.7-alpine  
  
ADD . /awesomeshop  
  
RUN apk update && \  
apk add --update \  
gcc \  
git \  
libjpeg-turbo \  
jpeg-dev \  
libffi \  
libffi-dev \  
libpng \  
libpng-dev \  
linux-headers \  
musl-dev \  
nodejs \  
openssl-dev \  
python-dev \  
zlib-dev && \  
pip install -r /awesomeshop/requirements.txt && \  
pip install uwsgi && \  
npm install -g bower && \  
cd /awesomeshop && \  
sed -i 's/bower install/bower --allow-root install/' init_webroot.sh && \  
./init_webroot.sh && \  
apk del gcc \  
git \  
jpeg-dev \  
libffi-dev \  
libpng-dev \  
linux-headers \  
musl-dev \  
nodejs \  
openssl-dev \  
python-dev \  
zlib-dev && \  
rm /var/cache/apk/* && \  
rm /awesomeshop/webroot/libs && \  
cp -a /awesomeshop/front/libs /awesomeshop/webroot/ && \  
rm -fr /awesomeshop/webroot/l10n && \  
cp -a /awesomeshop/translations /awesomeshop/webroot/l10n  
  
VOLUME /awesomeshop/webroot  
  
CMD ["uwsgi", "--socket", ":3031", "--chdir", "/awesomeshop", "--mount",
"/api=wsgi:app", "--manage-script-name", "--master"]  

