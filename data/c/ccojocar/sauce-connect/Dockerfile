# Dockerfile for Sauce Connect  
# https://docs.saucelabs.com/reference/sauce-connect/  
FROM debian:jessie  
  
MAINTAINER Cosmin Cojocar <cosmin.cojocar@protonmail.ch>  
  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Set environment variables  
ENV SC_VERSION 4.3.10  
ENV SAUCE_USERNAME sauce-username  
ENV SAUCE_ACCESS_KEY 865f37c5-92f1-41fa-b883-38de24b27dfc  
ENV TUNNEL_ID tunnel-id  
  
# Download and extract Sauce Conenct  
RUN curl https://saucelabs.com/downloads/sc-$SC_VERSION-
linux.tar.gz\?_ga\=1.8710773.1924683224.1439389020 | tar -xz --directory /opt  
RUN mv /opt/sc-$SC_VERSION-linux /opt/sc-linux  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare the entry point  
COPY docker-entrypoint.sh /opt/sc-linux/entrypoint.sh  
  
# Run  
ENTRYPOINT ["/opt/sc-linux/entrypoint.sh"]  
  
# Expose the TCP ports  
EXPOSE 4445

