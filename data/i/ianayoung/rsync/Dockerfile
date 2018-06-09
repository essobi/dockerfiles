FROM alpine:latest  
LABEL maintainer "ian@iay.org.uk"  
  
#  
# Add packages:  
#  
# Principal functionality is provided by openssh-client and rsync.  
#  
# bash is added for the benefit of some GitLab CI configurations which  
# assume bash functionality as part of secret key injection.  
#  
# --no-cache downloads the package database and then removes it  
# after package installation so that it doesn't take up space in the  
# final image.  
#  
RUN apk add --no-cache \  
bash \  
git \  
openssh-client \  
rsync  
  
CMD ["/bin/bash"]  

