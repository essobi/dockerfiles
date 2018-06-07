FROM fedora:24  
MAINTAINER Gerard Braad <me@gbraad.nl>  
  
RUN dnf update -y && \  
dnf install -y nodejs npm && \  
dnf clean all  
  
RUN npm install -g gitbook-cli && \  
gitbook install 3.2.0  
  
RUN mkdir -p /workspace  
VOLUME /workspace  
WORKDIR /workspace  
  
EXPOSE 4000  
EXPOSE 35729  
# Add tini (download, until package created)  
ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini /bin/tini  
RUN chmod +x /bin/tini  
ENTRYPOINT ["/bin/tini", "--"]  
  
CMD ["gitbook", "serve", "/workspace"]  
  

