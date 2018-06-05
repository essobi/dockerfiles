# http://wiki.centos.org/Download  
# http://mirror.symnds.com/distributions/CentOS-vault/2.1/final/isos/  
# https://docs.docker.com/articles/baseimages/  
# https://en.wikipedia.org/wiki/CentOS#Versioning_and_releases  
# http://bethesignal.org/blog/2011/01/05/how-to-mount-virtualbox-vdi-image/  
  
# Build the tar:  
# \- # Set up centos on vbox image (default options, except unselecting as
much  
# # instalation as possible)  
# \- VMDIR=<path_to_vbox_vm>  
# \- sudo modprobe nbd  
# \- sudo qemu-nbd -c /dev/nbd0 -r $VMDIR/Centos2.1.vdi  
# \- sudo mount /dev/nbd0p1 /mnt  
# \- sudo tar cf $(pwd)/centos-2.1.tar -C /mnt .  
# \- sudo umount /mnt  
  
# Build the image:  
# \- docker build -t centos-2.1 .  
  
# If you want to install packages:  
# \- # get centos 2.1 isos  
# \- sudo mkdir cd{1,2}  
# \- sudo mount -o loop 2.1-i386-disc1.iso cd1  
# \- sudo mount -o loop 2.1-i386-disc2.iso cd2  
# \- docker run -v $(pwd)/cd1:/cd1 -v $(pwd)/cd2:/cd2 -i -t centos-2.1 bash  
  
FROM scratch  
ADD centos-2.1.tar.gz /  

