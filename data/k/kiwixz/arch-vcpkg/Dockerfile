FROM kiwixz/arch  
  
ADD "bootstrap.sh" "/tmp/bootstrap.sh"  
RUN bash "/tmp/bootstrap.sh"  
  
RUN rm -rf \  
/tmp/* \  
/var/cache/pacman/pkg/* \  
/var/lib/pacman/sync/* \  
/var/tmp/*  

