FROM ubuntu:wily  
MAINTAINER Xi Shen <davidshen84@gmail.com>  
  
LABEL os=ubuntu:wily python=python27 gae=1.9.33 nodejs=5  
  
RUN apt-get update && apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential python-dev libjpeg8-dev zlib1g-dev
libfreetype6-dev liblcms2-dev  
RUN apt-get install -y unzip python-pip openssh-server git nodejs  
RUN apt-get install -y zsh  
RUN apt-get autoremove && apt-get clean  
  
RUN curl 'https://storage.googleapis.com/appengine-
sdks/featured/google_appengine_1.9.33.zip' -o /tmp/gae.zip  
RUN unzip /tmp/gae.zip -d /usr/local/src/  
RUN rm /tmp/gae.zip  
RUN ln -s /usr/include/freetype2 /usr/include/freetype2/freetype  
  
RUN npm install -g bower gulp-cli  
  
# allow root login with password  
RUN echo root:root | chpasswd  
RUN sed -e 's/\\(PermitRootLogin\\) without-password/\1 yes/' -i
/etc/ssh/sshd_config  
  
RUN mkdir -p /var/run/sshd  
  
VOLUME /usr/local/src/app  
WORKDIR /usr/local/src/app  
  
EXPOSE 22 8080 8000  
ENTRYPOINT /usr/sbin/sshd -De 2>&1  

