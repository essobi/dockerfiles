FROM ubuntu  
MAINTAINER Nicolas Delhomme (nicolas.delhomme@umu.se)  
  
#########  
### Aptitude packages  
#########  
RUN apt-get update  
RUN apt install -y build-essential curl unzip zip apache2 libghc-zlib-dev
locales supervisor  
  
#########  
### Squash locale warnings  
#########  
RUN rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
#########  
### Working dir  
#########  
RUN mkdir build  
WORKDIR /build  
  
#########  
## create the User  
#########  
RUN groupadd -g 2000 training && useradd -m -u 2000 -g 2000 training  
RUN echo 'training:training' | chpasswd  
RUN chsh -s /bin/bash training  
RUN echo "alias ll='ls -la -G'" >> /home/training/.profile  
RUN usermod -G training,www-data training  
  
#########  
### JBrowse dep  
#########  
RUN cpan App::cpanminus && cpanm PerlIO::gzip  
  
#########  
### JBrowse to easily view biological data formats  
#########  
RUN rm -f /var/www/html/index.html  
WORKDIR /var/www/html  
# -L is needed as GitHub redirects to AWS S3  
RUN curl -L -O
https://github.com/GMOD/jbrowse/releases/download/1.12.4-release/JBrowse-1.12.4.zip
&& \  
unzip JBrowse-1.12.4.zip  
WORKDIR /var/www/html/JBrowse-1.12.4  
RUN ./setup.sh && \  
chown -R www-data:www-data /var/www/html  
WORKDIR /  
RUN rm /var/www/html/JBrowse-1.12.4.zip  
  
#########  
### Cleanup  
#########  
WORKDIR /  
RUN rm -rf build  
  
#########  
### accessibility  
#########  
VOLUME /var/www/html/JBrowse-1.12.4/data  
EXPOSE 80  
#########  
### supervisord  
#########  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

