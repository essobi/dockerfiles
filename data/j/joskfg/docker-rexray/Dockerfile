FROM debian:latest  
MAINTAINER Jose Manuel Cardona <josemanuel.cardona@softonic.com>  
ENV REXRAY_VERSION=0.5.1 \  
AWS_ACCESS_KEY_ID="ACCESS KEY MISSING, provide it as environment variable" \  
AWS_SECRET_ACCESS_KEY="SECRET KEY MISSING, provide it as environment variable"
\  
AWS_SECURITY_GROUP_ID="SECURITY GROUP IDENTIFIER, provide it as environment
variable" \  
AWS_DEFAULT_REGION="eu-west-1"  
RUN apt-get update && apt-get install -y curl && apt-get clean \  
&& curl -sSL https://dl.bintray.com/emccode/rexray/install | sh -s -- stable
${REXRAY_VERSION}  
COPY entrypoint.sh /entrypoint.sh  
CMD /entrypoint.sh  

