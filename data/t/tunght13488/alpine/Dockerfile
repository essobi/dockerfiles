FROM alpine  
MAINTAINER Tung Ha "tunght13488@gmail.com"  
# Install common stuff  
# - bash: essential, I don't want to use #!/bin/sh all the time  
# - grep: looks like busybox grep is slow:
http://matthewkwilliams.com/index.php/2015/04/19/docker-containers-smaller-is-
not-always-better/  
RUN apk add --update \  
bash \  
grep \  
&& rm -rf /var/cache/apk/*  

