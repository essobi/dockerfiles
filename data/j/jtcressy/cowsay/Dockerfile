FROM fedora:25  
RUN dnf install procps-ng cowsay fortune-mod -y  
RUN cp -R /usr/share/games/fortune/* /fortunes/  
RUN cp -R /usr/share/games/fortune/* /default-fortunes/  
RUN ln -s /fortunes /usr/share/games/fortune  
VOLUME /fortunes  
ENV COWSAY_DURATION "10"  
ENV COWSAY_ANIMAL "default"  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

