FROM bryanhong/aptly  
  
# creating the aptly repo  
RUN mkdir /debs  
  
# may be install some ui for automating  
# -> vpn or ssh key generation / add  
# -> add new deb files  
# -> snapshot aptly version  
COPY entrypoint.sh /opt/  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["bash"]  

