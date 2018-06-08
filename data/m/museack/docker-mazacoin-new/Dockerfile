# version 1.4-1  
# docker-version 0.9.1  
FROM phusion/baseimage:0.9.13  
MAINTAINER guruvan "guruvan@maza.club"  
# We use a bootstrap script to avoid having temporary cache files and build  
# dependencies being committed and included into the docker image.  
COPY . /tmp  
RUN chmod +x /tmp/bootstrap.sh && /tmp/bootstrap.sh  
# Uncomment the follwing line if you prefer to run without  
# the wallet volume  
#VOLUME ["/home/maza"]  
# If you use the following line, you MUST  
# run with a wallet data container OR  
# understand your wallet is EPHEMERAL!!  
#  
# In our wallet container, we make /home/wallets/.container  
# to know when we've added it our selves  
VOLUME ["/home/maza","/home/wallets"]  
  
#XPOSE RPC P2P Testnet  
EXPOSE 12832 12835 11832 11835 22  
#ENTRYPOINT [""]  
CMD ["/sbin/my_init"]  

