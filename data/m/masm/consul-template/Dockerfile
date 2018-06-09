FROM masm/archlinux  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
ENTRYPOINT ["/usr/bin/consul-template"]  
  
RUN pacman -S unzip --needed --noconfirm --noprogressbar  
RUN curl -sSL https://releases.hashicorp.com/consul-template/0.12.2/consul-
template_0.12.2_linux_amd64.zip > /tmp/consul.zip && \  
unzip /tmp/consul.zip -d /tmp && \  
mv /tmp/consul-template /usr/bin/consul-template && \  
rm -f /tmp/consul.zip  

