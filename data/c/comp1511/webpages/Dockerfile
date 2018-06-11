FROM bitnami/minideb:unstable  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_AU.UTF-8  
ENV LANGUAGE en_AU:en  
ENV LC_ALL en_AU.UTF-8  
  
EXPOSE 5000  
  
RUN \  
rm /etc/localtime &&\  
cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime &&\  
echo Australia/Sydney >/etc/timezone &&\  
install_packages locales &&\  
localedef -i en_AU -c -f UTF-8 -A /usr/share/locale/locale.alias en_AU.UTF-8
&&\  
install_packages \  
make git rsync \  
python3 python3-flask python3-jinja2 python3-lxml python3-html5lib python3-bs4
python3-ldap3 python3-toml python3-dateutil python3-pygments  
  
RUN \  
mkdir -p /web/cs2041/bin/ &&\  
ln -s /usr/bin/python3 /web/cs2041/bin/python3.6.3  
  
ADD /entrypoint entrypoint  
ENTRYPOINT ["/entrypoint"]  

