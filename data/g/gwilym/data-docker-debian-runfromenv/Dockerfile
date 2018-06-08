FROM debian:jessie  
  
RUN apt-get -qy update \  
&& apt-get -qy upgrade \  
&& apt-get -qy install unzip \  
&& apt-get -qy clean  
  
COPY run-from-env.sh /bin/run-from-env.sh  
CMD ["/bin/run-from-env.sh"]  

