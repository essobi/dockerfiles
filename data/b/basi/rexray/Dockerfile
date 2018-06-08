FROM debian:latest  
  
MAINTAINER Basilio Vera <basilio.vera@softonic.com>  
  
ENV REXRAY_VERSION=0.3.3 \  
AWS_ACCESS_KEY_ID="ACCESS KEY MISSING, provide it as environment variable" \  
AWS_SECRET_ACCESS_KEY="SECRET KEY MISSING, provide it as environment variable"  
RUN apt-get update && apt-get install -y curl && apt-get clean \  
&& curl -sSL https://dl.bintray.com/emccode/rexray/install | sh -s -- stable
${REXRAY_VERSION}  
  
COPY entrypoint.sh /entrypoint.sh  
  
CMD /entrypoint.sh  

