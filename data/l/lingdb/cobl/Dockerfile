FROM alpine:latest  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="cobl" \  
version="1.6.0" \  
documentation="https://github.com/lingdb/container/wiki/cobl"  
  
RUN apk update \  
&& apk add \  
python3 python3-dev \  
postgresql-dev \  
build-base \  
vim \  
less \  
git \  
nodejs \  
&& rm /var/cache/apk/APKINDEX*tar.gz \  
&& npm install --global bower grunt-cli \  
&& git config --global url."https://".insteadOf "git://"  
  
# Installing pip dependencies:  
COPY CoBL/REQUIREMENTS /REQUIREMENTS  
RUN pip3 install --upgrade pip \  
&& pip3 install -r /REQUIREMENTS \  
&& rm /REQUIREMENTS  
  
# Installing {npm,bower} dependencies:  
COPY CoBL/static /build_static  
WORKDIR /build_static  
RUN npm install \  
&& bower install --allow-root ./bower.json \  
&& grunt  
  
# Readying CoBL directory:  
COPY CoBL /CoBL  
RUN rm -rf /CoBL/static \  
&& mv /build_static /CoBL/static  
  
# Creating copyStatic:  
RUN mkdir /copyStatic  
  
# local_settings.py  
RUN cp /CoBL/ielex/local_settings.py.dist /CoBL/ielex/local_settings.py  
  
# Getting ready to run:  
WORKDIR /CoBL  
EXPOSE 5000  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

