FROM alpine:edge  
MAINTAINER Jesse Wei "web.jesse@gmail.com"  
#  
# INSTALL  
#  
RUN apk add --no-cache bash sed grep coreutils  
  
# SETUP  
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd  
  
# COMMAND  
CMD ["bash"]

