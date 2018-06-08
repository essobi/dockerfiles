FROM java:openjdk-8-jre  
MAINTAINER Markus Mayer <widemeadows@gmail.com>  
  
ENV VERSION 0.27.2  
ENV ARCHIVE
https://s3.amazonaws.com/name.abuchen.portfolio/${VERSION}/PortfolioPerformance-${VERSION}-linux.gtk.x86_64.tar.gz  
  
ENV DISPLAY=:0  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install libgtk2.0-0 libcanberra-gtk-
module libwebkitgtk-1.0.0 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash portfolio && mkdir /data && chown portfolio /opt
/data  
USER portfolio  
  
RUN cd /opt && (curl ${ARCHIVE} | tar xvz)  
  
WORKDIR /data  
CMD /opt/portfolio/PortfolioPerformance  

