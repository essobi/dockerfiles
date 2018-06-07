FROM fedora:latest as builder  
RUN echo "%_install_langs en" >/etc/rpm/macros.image-language-conf \  
&& dnf install --setopt=deltarpm=0 --setopt=tsflags=nodocs -y \  
gcc libffi-devel libjpeg-devel libsodium-devel libxml2-devel \  
libxslt-devel openssl-devel postgresql-devel python2-devel python2-virtualenv
\  
redhat-rpm-config rpm-build  
ENV SYNAPSE_VERSION="0.30.0"  
ENV VENV=/buildroot/opt/synapse  
RUN mkdir -p $VENV  
RUN python2 -m virtualenv $VENV  
RUN $VENV/bin/pip install no-manylinux1  
RUN SODIUM_INSTALL=system $VENV/bin/pip install https://github.com/matrix-
org/synapse/archive/v$SYNAPSE_VERSION.tar.gz lxml 'Twisted>=17.1.0' psycopg2  
WORKDIR /buildroot  
ENV RPM_BUILD_ROOT=/buildroot  
RUN /usr/lib/rpm/brp-python-bytecompile  
RUN find $RPM_BUILD_ROOT | /usr/lib/rpm/redhat/find-requires | grep -v
"^$RPM_BUILD_ROOT" \  
| xargs rpm -q --whatprovides --qf='%{name}.%{arch}\n' | sort -u >
$VENV/requires.txt  
RUN find $VENV/lib/python2.7/site-packages -type f -executable -exec objcopy
--compress-debug-sections {} \;  
  
FROM fedora:latest  
COPY start.sh /  
COPY \--from=builder /buildroot/opt/synapse /opt/synapse  
RUN echo "%_install_langs en" >/etc/rpm/macros.image-language-conf \  
&& dnf install --setopt=deltarpm=0 --setopt=tsflags=nodocs -y $(cat
/opt/synapse/requires.txt) \  
&& rm -rf /var/cache/dnf/* /etc/rpm/macros.image-language-conf \  
&& groupadd -r -g 797 docker && useradd -r -g docker -u 797 docker \  
&& mkdir /data && chown docker:docker /data  
VOLUME ["/data"]  
EXPOSE 8448  
ENTRYPOINT /start.sh  
USER docker  

