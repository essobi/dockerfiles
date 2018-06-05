FROM gcr.io/google_containers/ubuntu-slim:0.6  
# Ensure there are enough file descriptors for running Fluentd.  
RUN ulimit -n 65536  
  
# Disable prompts from apt.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy the Fluentd configuration file.  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
  
COPY build.sh /tmp/build.sh  
RUN bash /tmp/build.sh  
  
ENV LD_PRELOAD /opt/td-agent/embedded/lib/libjemalloc.so  
  
# Add config file and self-signed certificate  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
COPY certificate.pem /etc/ssl/certificate.pem  
COPY key.pem /etc/ssl/key.pem  
  
# Run the Fluentd service.  
ENTRYPOINT ["td-agent"]  

