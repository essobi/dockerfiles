FROM debian:testing  
  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER Bertrand Roussel "broussel@sierrawireless.com"  
RUN apt-get -qq update && \  
apt-get upgrade -qy && \  
apt-get -qy install apt-utils gettext-base \  
fcgiwrap git cgit highlight perl \  
ca-certificates nginx gettext-base \  
markdown python-docutils groff && \  
echo 'UTC' > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add Tini  
ENV TINI_VERSION v0.13.2  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
RUN useradd nginx  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
RUN mkdir /srv/git  
  
VOLUME ["/srv/git"]  
VOLUME ["/var/cache/cgit"]  
  
COPY cgitrc.template /etc/  
  
COPY syntax-highlighting.sh /usr/lib/cgit/filters/  
  
COPY default.conf /etc/nginx/sites-available/default  
  
COPY 404.html /usr/share/nginx/html/  
COPY 401.html /usr/share/nginx/html/  
  
COPY startup /  
CMD ["/startup"]  
  
ENV CGIT_TITLE "My cgit interface"  
ENV CGIT_DESC "Super fast interface to my git repositories"  
ENV CGIT_VROOT "/"  
ENV CGIT_SECTION_FROM_STARTPATH 0  

