FROM suckowbiz/base  
  
LABEL maintainer="Tobias Suckow <tobias@suckow.biz>"  
  
RUN apt-get install --quiet --quiet --yes --no-install-recommends \  
tor \  
tor-geoipdb \  
&& apt-get clean  
  
EXPOSE 9095  
ENTRYPOINT ["tor", "SocksPort", "0.0.0.0:9050"]  
CMD ["ExcludeExitNodes", "{de}"]  

