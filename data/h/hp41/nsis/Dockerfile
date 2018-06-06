FROM debian:experimental  
ENV NSIS_VERSION 3.01-1  
RUN apt-get -t experimental update && \  
apt-get -t experimental install -y nsis=${NSIS_VERSION} && \  
apt-get clean  
ENTRYPOINT ["makensis", "-V4"]

