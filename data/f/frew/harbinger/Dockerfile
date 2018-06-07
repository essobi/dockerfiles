FROM perl:5.20.1  
MAINTAINER Arthur Axel fREW Schmidt <frioux@gmail.com>  
  
ADD . /opt/harbinger  
WORKDIR /opt/harbinger  
  
RUN env DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install --no-install-recommends -y \  
libmysqlclient-dev \  
libpq-dev \  
&& apt-get autoremove -y \  
&& cpanm -n --installdeps . \  
&& cpanm -n DBD::Pg DBD::mysql DateTime::Format::Pg DateTime::Format::MySQL \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cpanm
local/cache local/man  
  
EXPOSE 8001  
CMD ["perl", "-Ilib", "bin/harbinger-server"]  

