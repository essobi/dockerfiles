#########################################################################################  
#  
# Rebuild a CoreOS iPXE image.  
# https://github.com/SojournLabs/netboot  
#  
#########################################################################################  
  
# Usage:  
# docker run  
# --env PLATFORM=[metal|virtual]  
# -v /path/to/certificates:/vapr/certstore:ro  
# -v /path/to/coreos/images:/vapr/images:ro  
# -v /path/to/output/directory:/vapr/build  
# --rm -t -i sojournlabs/recore [bootserver|node]  
  
FROM sojournlabs/squashfs_tools  
MAINTAINER jonathan lung <auto+vapr@heresjono.com>  
ADD recore /bin/recore  
ADD profiles /vapr/profiles  
ENTRYPOINT ["/bin/recore"]  

