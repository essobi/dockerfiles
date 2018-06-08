# progrium/cedarish:cedar14 was segfaulting on ruby for some reason.  
# So, using latest version as the base instead  
FROM progrium/cedarish  
MAINTAINER Matthew Landauer <matthew@oaf.org.au>  
  
RUN mkdir /app  
  
# Commented out to see if it's needed anymore now that we're not running  
# commands inside of a shell  
# # Get rid of annoying error message "stdin: is not a tty"  
# ADD profile /root/.profile  
# Add certificate authority used by mitmproxy  
# Also needs to be identical to the cert at mitmproxy/mitmproxy-ca-cert.pem in  
# https://github.com/openaustralia/morph  
ADD mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy-ca-
cert.crt  
RUN update-ca-certificates  
  
# Add prerun script which will disable output buffering for ruby  
ADD prerun.rb /usr/local/lib/prerun.rb  
  
# poppler-utils has a more recent pdftohtml than the pdftohtml package  
# pdftohtml is needed by the python scraperwiki library  
# libffi-dev needed by python cffi  
# time is needed directly by morph.io for scraper run measurements  
RUN apt-get update && apt-get install -y time libblas-dev liblapack-dev
gfortran swig protobuf-compiler libprotobuf-dev libsqlite3-dev poppler-utils
libffi-dev phantomjs  
  
# Make python pip use the new ca certificate. Wouldn't it be great if it used  
# the system ca certificates by default? Well, it doesn't.  
# Setting the PIP_CERT environment variable didn't work but this does  
# TODO Remove this once compiles don't send traffic to mitmproxy  
ADD pip.conf /etc/pip.conf  

