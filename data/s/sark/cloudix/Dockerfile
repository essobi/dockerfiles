FROM scratch  
ADD cloudix-linux-fs.tar.bz2 /  
  
# minor docker-specific tweaks  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# overwrite this with 'CMD []' in a dependent Dockerfile  
CMD ["/bin/bash"]  

