  
FROM iaghidro/base:latest  
  
# Set user  
USER root  
  
COPY ./container-scripts/ /container-scripts/wallet-apps  
  
# Run provisioning script  
RUN /container-scripts/wallet-apps/createWalletApps.sh  

