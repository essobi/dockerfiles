FROM opensuse:13.2  
MAINTAINER Jeff Bonhag <jbonhag@sca-corp.com>  
  
RUN zypper --gpg-auto-import-keys ref  
  
RUN zypper --non-interactive in curl tar gcc gcc-c++ gettext make \  
ca-certificates unzip autoconf libtool which apache2 apache2-devel sqlite3 ed  
  
RUN mkdir /cache  
WORKDIR /cache  
  
RUN echo $PATH  
  
RUN curl http://download.mono-project.com/sources/mono/mono-3.6.0.tar.bz2 | \  
tar xjf - -C /cache && cd /cache/mono-3.6.0 && ./configure && \  
make && make install  
  
RUN curl -O https://github.com/mono/mod_mono/archive/3.8.zip && unzip 3.8.zip
&& \  
cd mod_mono-3.8 && ./autogen.sh && make install  
  
RUN curl -O https://github.com/mono/xsp/archive/3.0.11.zip && \  
unzip 3.0.11.zip && cd xsp-3.0.11 && ./autogen.sh && make install  
  
# now, we dance  
RUN curl https://bitbucket.org/jbonhag/wcfservice1/get/v0.0.1.tar.gz | \  
tar zxf - -C /srv/www/htdocs && cd /srv/www/htdocs/ && ls  
  
# BUILD  
RUN xbuild  
  
# DEPLOY  
USER root  
RUN mv WcfService1 /srv/www/htdocs/  
RUN ed -s /etc/apache2/httpd.conf <<< $'185d\nw'  
RUN echo Include /etc/apache2/mod_mono.conf >> /etc/apache2/httpd.conf  
RUN echo MonoServerPath /usr/local/bin/mod-mono-server4 >>
/etc/apache2/httpd.conf  
RUN echo AddType application/x-asp-net .svc >> /etc/apache2/httpd.conf  
  
# RUN  
USER root  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

