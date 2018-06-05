FROM concourse/buildroot:curl  
  
ENV BOSH_CLI_VERSION "2.0.16"  
ADD assets/ /opt/resource/  
RUN chmod +x /opt/resource/*  
  
RUN curl -L "https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-${BOSH_CLI_VERSION}-linux-amd64" -o /usr/bin/bosh \  
&& chmod +x /usr/bin/bosh  

