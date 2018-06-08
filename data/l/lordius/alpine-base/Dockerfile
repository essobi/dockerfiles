# lordius/alpine-base:v3.7  
FROM alpine:3.7  
LABEL maintainer=andriy.khomych@gmail.com  
  
# Update indexed.  
RUN apk --no-cache update \  
apk --no-cache upgrade  
  
# Install aditional software, for me nano editor.  
RUN apk add --no-cache autoconf postfix icu-dev\  
apk-cron ca-certificates curl-dev libcurl \  
bash build-base diffutils git \  
imagemagick imap less libtool linux-headers musl \  
nano openssl patch patchutils gcc g++ make \  
pcre-dev fcgi-dev jpeg-dev libmcrypt-dev bzip2-dev \  
tar wget xz zlib-dev imagemagick-dev sed re2c m4 acl-dev \  
libpng-dev libxslt-dev postgresql-dev perl-dev file libedit-dev \  
libxml2-dev imap-dev cyrus-sasl-dev rsync p7zip python py-lxml py-pip \  
sshpass sudo  
  
# Install ansible.  
RUN apk --update add --virtual \  
build-dependencies \  
python-dev \  
musl-dev \  
libffi-dev && \  
pip install --upgrade pip  
  
  
RUN pip install git+git://github.com/ansible/ansible.git@stable-2.2  
  
# Install ssh.  
RUN apk add --update openssh  
  
# Configure git.  
RUN git config --global user.name "Lordius Base" && \  
git config --global user.email "admin@lordius.com" && \  
git config --global push.default current  
  
# Clean trash.  
RUN rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /var/www/localhost/htdocs/*  

