FROM alpine:edge  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE "openssh tzdata"  
# Install package using --no-cache to update index and remove unwanted files  
RUN apk add --update --no-cache $PACKAGE && \  
cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime && \  
echo "Australia/Sydney" > /etc/timezone && \  
# Add a user to run as non root  
adduser -D -g '' sshel && \  
# Disable password-based access to an account while allowing SSH access  
sed -i "s/sshel:!/sshel:*/g" /etc/shadow && \  
# Disable root access  
sed -i "s/root:/root:!/g" /etc/shadow  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  
  

