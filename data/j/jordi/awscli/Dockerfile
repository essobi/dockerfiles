FROM debian:wheezy  
  
MAINTAINER Jordi Íñigo  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends less curl ca-certificates unzip
groff-base python && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && rm -rf /tmp  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
ENV LANG C.UTF-8  
ENTRYPOINT ["/usr/local/bin/aws"]  
  
CMD ["help"]

