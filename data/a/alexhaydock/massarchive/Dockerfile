FROM alpine:3.7  
LABEL maintainer "Alex Haydock <alex@alexhaydock.co.uk>"  
  
RUN set -xe \  
\  
# Install Python and OpenSSL (OpenSSL is needed because the requests module
uses it for HTTPS connections)  
&& apk update \  
&& apk add python2 py2-pip openssl \  
\  
# Add Python dependencies (For a list, see:
https://github.com/motherboardgithub/mass_archive)  
&& pip install requests archiveis  
  
# Download mass_archive  
ADD
https://raw.githubusercontent.com/motherboardgithub/mass_archive/master/mass_archive.py
/opt/mass_archive.py  
  
# Run  
ENTRYPOINT ["python2","/opt/mass_archive.py"]  

