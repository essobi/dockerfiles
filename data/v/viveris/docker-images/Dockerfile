FROM hrishikesh/libvirtd  
  
RUN yum install -y libguestfs-tools  
  
# To use directly qemu without using libvirt  
ENV LIBGUESTFS_BACKEND direct  
  
CMD ["guestmount", "--version"]  

