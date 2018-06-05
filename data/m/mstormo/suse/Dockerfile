#
==============================================================================  
# How To Create a Minimal Docker Base Layer in 10 Easy Steps  
#
\------------------------------------------------------------------------------  
# (2015) Marius Storm-Olsen <mstormo@gmail.com>  
#  
# 1\. Create a JeOS with SUSE Studio (https://susestudio.com)  
#  
# 2\. Build and download the USB Stick / Hard Disk Image  
#  
# 3\. Unpackage the image file  
# tar zxvf <image.tar.gz>  
#  
# 4\. Run  
# fdisk -l <image file.raw>  
# to get the image file's configuration, paying attention to the file system  
# type, "sector size" and "start" sector. Your offset into the image will be  
# "start sector" and "sector size", f.ex:  
# start sector: 2048  
# *sector size: 512  
# =img offset: 1048576  
#  
# 5\. Loop mount the file system:  
# sudo mount -t <type> -o ro,loop,offset=<offset> <image.raw> /mnt/temp  
#  
# 6\. Package the content into a tar gz file:  
# sudo tar -C /mnt/temp -c . > rootfs.tar  
# gzip rootfs.tar  
#  
# 7\. Setup Dockerfile with the full rootfs, and add a script with packages
you  
# want to remove, and other cleanups and fixes you want to do:  
# FROM scratch  
# ADD rootfs.tar.gz /  
# COPY sles11sp4_minimize.sh /root/  
# RUN chmod 0755 /root/sles11sp4_minimize.sh  
#  
# 8\. Run  
# docker build .  
# docker run -ti <image> /bin/bash  
# $ /root/sles11sp4_minimize.sh  
#  
# # Note: I personally like to leave my trail visible for people to see so  
# # they know what changes, have been made to the original image, and not do  
# # f.ex.  
# # $ rm /root/sles11sp4_minimize.sh  
# # $ history -c  
# # But, that's entirely up to you as an image maintainer of course.  
#  
# $ exit  
#  
# 9\. Export the container as a new base layer, and compress it as much as  
# possible for distribution:  
# docker export <container> > sles-11-sp4-x86_64.tar  
# xz -9 -e sles-11-sp4-x86_64.tar  
#  
# 10\. Change Dockerfile to simply use the new image as its base  
#  
#
==============================================================================  
  
FROM scratch  
ADD sles-11-sp4-x86_64.tar.xz /  

