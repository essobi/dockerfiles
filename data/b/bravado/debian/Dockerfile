FROM debian:stretch  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends
--no-install-suggests -y \  
gettext-base locales supervisor ca-certificates unzip curl gnupg \  
apt-transport-https \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*.log  
  
# Set the locale  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Configure timezone and locale  
RUN cp "/usr/share/zoneinfo/America/Sao_Paulo" /etc/localtime \  
&& localedef -i pt_BR -f UTF-8 pt_BR.UTF-8  
  
ADD etc /etc  
  
RUN chmod +x /etc/entrypoint.sh \  
&& mkdir /etc/entrypoint.d  
  
ENTRYPOINT '/etc/entrypoint.sh'  

