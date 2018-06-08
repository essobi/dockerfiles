# arch-loris  
FROM openmarble/arch-imaging:latest  
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>  
  
RUN cd /build  
  
WORKDIR /opt  
# Get loris and unzip.  
# TODO: Move to specific tag later  
RUN curl -LO https://github.com/loris-
imageserver/loris/archive/development.zip \  
&& unzip development.zip \  
&& mv loris-development/ loris/ \  
&& rm development.zip  
  
RUN useradd -d /var/www/loris -s /sbin/false loris  
  
RUN pip install -r loris/requirements.txt  
  
RUN pip install ./loris  
  
# Create image directory  
RUN mkdir /usr/local/share/images  
# Load example images  
RUN cp -R loris/tests/img/* /usr/local/share/images/  
  
COPY loris2.conf etc/loris2.conf  
COPY webapp.py /opt/loris/loris/webapp.py  
  
WORKDIR /opt/loris/loris  
  
EXPOSE 5004  
CMD ["python", "webapp.py"]  

