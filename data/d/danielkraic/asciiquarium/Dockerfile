FROM fedora:23  
MAINTAINER Daniel Kraic <danielkraic@gmail.com>  
  
RUN dnf install -y perl-Term-Animation && dnf clean all  
RUN curl -s -o /opt/asciiquarium
https://raw.githubusercontent.com/cmatsuoka/asciiquarium/master/asciiquarium  
  
CMD ["perl", "/opt/asciiquarium"]  

