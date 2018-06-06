FROM buildpack-deps:trusty  
MAINTAINER Software Craftsmen GmbH & Co KG <office@software-craftsmen.at>  
  
ENV CONFLUENCE_VERSION=6.3.1-x64  
  
RUN wget --no-verbose
https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-$CONFLUENCE_VERSION.bin -O atlassian-
confluence-$CONFLUENCE_VERSION.bin && \  
chmod a+x atlassian-confluence-$CONFLUENCE_VERSION.bin  
  
# Run the installer  
# The response file is produced by an attended installation at
/opt/atlassian/confluence/.install4j/response.varfile  
ADD response.varfile response.varfile  
# Run unattended installation with input from response.varfile  
RUN ./atlassian-confluence-$CONFLUENCE_VERSION.bin -q -varfile
response.varfile && \  
rm atlassian-confluence-$CONFLUENCE_VERSION.bin  
  
# HTTP port  
EXPOSE 8090  
# Control port  
EXPOSE 8000  
# Adjust this path if the installation location has been modified by the
response.varfile  
CMD ["./opt/atlassian/confluence/bin/start-confluence.sh", "-fg"]  

