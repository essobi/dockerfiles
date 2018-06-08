FROM debian  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
RUN apt-get update  
RUN apt-get install -y \  
wget  
WORKDIR /installers/confluence  
ADD install_confluence /bin/install_confluence  
ADD response.varfile response.varfile  
RUN useradd --create-home -c "Atlassian Confluence" confluence  
VOLUME ["/var/confluence"]  
ADD CertAuthenticator.class /vapr/CertAuthenticator.class  
WORKDIR /var/confluence

