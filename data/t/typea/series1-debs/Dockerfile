FROM typea/package-builder:jessie  
  
ENV APP_DIR=/home/user  
ENV distro="jessie"  
USER root  
RUN echo "deb-src http://http.debian.net/debian ${distro} main" \  
> /etc/apt/sources.list.d/${distro}-src.list  
RUN apt-get update && apt-get install -y \  
bash-completion \  
config-package-dev \  
libavahi-compat-libdnssd1 \  
python-pip \  
gdebi-core \  
dh-python \  
dh-systemd \  
ruby \  
ruby-dev \  
ruby-nokogiri \  
python-pbkdf2 \  
devscripts  
  
RUN gem install deb-s3  
  
WORKDIR $APP_DIR  
USER user  
ADD requirements-dev.txt ${APP_DIR}/  
RUN pip install -r requirements-dev.txt --user  
ADD requirements-jessie.txt builder builder stdeb.cfg upload.sh ${APP_DIR}/  
#RUN chown -R user:user $APP_DIR  
CMD ./builder  

