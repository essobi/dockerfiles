FROM silintl/apache2:latest  
MAINTAINER "Phillip Shipley" <phillip_shipley@sil.org>  
  
ENV REFRESHED_AT 2017-01-06  
RUN apt-get update -y \  
&& apt-get clean  
  
COPY redirect.conf /etc/apache2/sites-enabled/  

