FROM debian:jessie  
  
LABEL Name="nikto from git" Author="Carlos Alberto Castelo Elias Filho
<cacefmail@gmail.com>"  
RUN buildDeps=' \  
git \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends\  
$buildDeps \  
ca-certificates \  
perl \  
libnet-ssleay-perl \  
libwhisker2-perl \  
&& git clone \--depth 1 https://github.com/sullo/nikto.git /opt/nikto \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN chmod 755 /opt/nikto/program/nikto.pl \  
&& mkdir /work \  
&& adduser -q --gecos "" \--disabled-password --shell /bin/bash user \  
&& chown -R user /work  
  
USER user  
WORKDIR /work  
  
VOLUME /work  
  
ENTRYPOINT ["perl", "/opt/nikto/program/nikto.pl"]  
CMD ["-H"]

