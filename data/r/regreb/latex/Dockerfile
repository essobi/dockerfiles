FROM bitnami/minideb:latest  
  
RUN install_packages texlive-full biber latexmk xzdec git make wget curl
locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG en_US.utf8  

