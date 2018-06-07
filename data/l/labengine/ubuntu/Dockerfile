FROM ubuntu  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
ENV TIMEZONE "Europe/Zurich"  
# Add buildpack ubuntu  
COPY script_base/ /root  
RUN chmod 775 /root/*.sh  
  
# Run buildpack  
RUN ./root/build_default_pack.sh  
  
# =>[ list php7 package => RUN apt-cache search php7-* ]  
# =>[ Expose ssh => EXPOSE 22 ]  
# pepare for takeoff  
CMD ["/bin/bash"]  

