FROM swift  
MAINTAINER Izzy Navedo <izzynavedo@gmail.com>  
  
# Install Vapor Toolbox.  
RUN curl -sL toolbox.vapor.sh | bash  
  
WORKDIR /root  
VOLUME /root  
EXPOSE 8080  
ENTRYPOINT ["vapor"]  
CMD ["--help"]  

