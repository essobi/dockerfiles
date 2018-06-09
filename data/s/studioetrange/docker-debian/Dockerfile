FROM debian:latest  
MAINTAINER StudioEtrange <nomorgan@gmail.com>  
  
# Debian package & stuff -------------  
RUN echo "deb http://http.debian.net/debian stable non-free" >>
/etc/apt/sources.list \  
&& echo "deb http://http.debian.net/debian stable-updates non-free" >>
/etc/apt/sources.list  
  
# DEBIAN packages  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
python \  
supervisor \  
unrar \  
unzip \  
curl \  
git \  
ca-certificates \  
pwgen \  
wget \  
nano \  
&& rm -rf /var/lib/apt/lists/*  
  
# SUPERVISOR -------------  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
# Supervisord web interface -------  
EXPOSE 9999  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

