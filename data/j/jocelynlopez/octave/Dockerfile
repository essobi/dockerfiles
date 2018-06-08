# ----------------------  
# Docker's informations:  
# ----------------------  
FROM python:3.6.4  
MAINTAINER Jocelyn LOPEZ <jocelyn.lopez.pro@gmail.com>  
  
# --------------------------  
# Install required packages:  
# --------------------------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
octave \  
&& rm -rf /var/lib/apt/lists/*  
  
# ---------  
# Settings:  
# ---------  
RUN adduser --home=/opt/octave --disabled-password --gecos ""
\--shell=/bin/bash octave  
RUN echo 'addpath(genpath("/app/lib/"))' >>
/usr/share/octave/site/m/startup/octaverc  
  
# -----------  
# Executable:  
# -----------  
ENTRYPOINT ["octave"]  

