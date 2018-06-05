# Axle-Base Dockerfile  
#  
# The container built from this Dockerfile serves no other purpose then to  
# expose and host volumes and bind-mounts. So a lean 1.5mb busybox image is  
# best for the job.  
#  
# Pull this image with `docker pull radial/axle-base` to use as a volume  
# container for bind mounts and other persistent data that needs access from  
# multiple containers.  
  
FROM radial/busyboxplus:base  
  
# Simple program to keep the container alive and do nothing  
COPY IDLE /usr/bin/IDLE  
CMD ["IDLE"]  

