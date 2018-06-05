FROM arnaudhb/ubuntu-dev:build-automation  
  
ENV IDE_ATOM_VERSION v1.15.0  
# Get Atom IDE  
ADD https://github.com/atom/atom/releases/download/$IDE_ATOM_VERSION/atom-
amd64.deb /src  
  
# Install Atom IDE  
RUN apt-get update && apt-get install -y \  
gconf2 \  
libnotify4 \  
python \  
gvfs-bin \  
&& dpkg -i '/src/atom-amd64.deb' \  
&& rm -rf /src/*.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
# Get Eclipse installer  
ADD http://ftp-stud.fht-
esslingen.de/pub/Mirrors/eclipse/oomph/products/eclipse-inst-linux64.tar.gz
/opt  
RUN cd /opt && tar xzf eclipse-inst-linux64.tar.gz  
  
# Cleanup  
RUN rm -f /opt/*.tar.gz  
  
# Exposed volume(s)  
VOLUME [ '/root/.atom' ]  
  
# Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod u+x /docker-entrypoint.sh  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

