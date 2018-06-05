FROM debian:stable-backports  
MAINTAINER Tobias Sette <contato@tobias.ws>  
LABEL version="0.1"  
LABEL description="Imagem básica do Debian com ajustes para o português do
Brasil"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN echo America/Sao_Paulo > /etc/timezone && dpkg-reconfigure tzdata  
RUN echo "locales locales/locales_to_be_generated multiselect pt_BR.UTF-8
UTF-8" | debconf-set-selections && \  
echo "locales locales/default_environment_locale select pt_BR.UTF-8" |
debconf-set-selections  
RUN apt-get update && apt-get install locales -qq  
ENV LC_ALL pt_BR.UTF-8  

