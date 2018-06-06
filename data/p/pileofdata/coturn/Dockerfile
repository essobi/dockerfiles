FROM google/debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
gdebi-core  
RUN curl -O http://turnserver.open-
sys.org/downloads/v4.1.2.1/turnserver-4.1.2.1-debian-wheezy-ubuntu-
mint-x86-64bits.tar.gz  
RUN tar xvfz turnserver*  
RUN gdebi -n coturn*.deb  
RUN rm coturn*  
RUN rm turnserver*  
RUN rm INSTALL  
  
CMD "turnserver --user-auth-secret -v -a -f --static-auth-secret notasecret -r
http://localhost:8080"  
  

