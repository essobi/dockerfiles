  
FROM ubuntu:14.10  
RUN sed -i 's/archive/old-releases/g' /etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y apt-transport-https  
RUN apt-get update  
  
RUN echo >> /etc/apt/sources.list  
RUN echo "deb https://idefix.biozentrum.uni-wuerzburg.de/ubuntu trusty main
universe" >> /etc/apt/sources.list  
RUN echo "deb-src https://idefix.biozentrum.uni-wuerzburg.de/ubuntu trusty
main universe" >> /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get install -y super-resolution-de-keyring --allow-unauthenticated  
RUN apt-get update  
RUN apt-get install -y rapidstorm  
  
RUN apt-get install -y xvfb  
  
RUN echo "xvfb-run -a rapidstorm \$* " >> go.sh  
  
ENV DISPLAY :1.0  
ENTRYPOINT ["bash","-x","go.sh"]  
  
CMD ["--Help"]  

