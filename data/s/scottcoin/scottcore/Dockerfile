FROM scottcoin/scottcoin:latest  
MAINTAINER "scottcoin"  
USER root  
  
# Load dependencies  
RUN apk add --update-cache \  
nodejs=4.3.0-r0  
  
WORKDIR /home/scottcoin/  
  
COPY scripts/* ./  
COPY scottnode/ ./.bitcore/  
RUN chown -R scottcoin:scottcoin .  
RUN ./build-node.sh  
  
# Expose ports for Insight and Wallet Service  
EXPOSE 8200  
EXPOSE 3232  
# Setup environment variables not set in Scottcoin with appropriate defaults  
ENV INSIGHT_WEB="false" \  
DB_NAME="mongo"  
USER scottcoin  
  
ENTRYPOINT ["./launch.sh"]  

