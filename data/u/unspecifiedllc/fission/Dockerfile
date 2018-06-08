FROM gcr.io/cloud-builders/kubectl  
  
ENV FISSION_URL
https://github.com/fission/fission/releases/download/0.6.0/fission-cli-linux  
  
RUN curl -Lo fission $FISSION_URL && chmod +x fission && mv fission
/usr/local/bin/  
  
COPY src/scripts /builder/fission/scripts  
  
ENTRYPOINT ["/builder/fission/scripts/fission.bash"]

