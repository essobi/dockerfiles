FROM debian  
LABEL maintainer=jooool  
  
# Update APT base then install dns-batch dependencies  
RUN apt-get update && apt-get install -y \  
sendemail \  
libio-socket-ssl-perl \  
ca-certificates \  
whois

