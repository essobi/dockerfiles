FROM fedora  
LABEL maintainer 'https://github.com/sjugge'  
  
RUN dnf up -y && \  
dnf install -y dnf-plugins-core && \  
dnf copr enable -y daftaupe/hugo && \  
dnf install -y hugo  
  
EXPOSE 1313  
WORKDIR /app  
  
CMD hugo server \  
# --disableFastRender \  
\--bind="0.0.0.0" \  
\--source=/app \  
\--destination=/app/public  

