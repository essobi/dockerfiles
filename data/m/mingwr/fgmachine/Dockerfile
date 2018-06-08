  
# Start with Keras base image  
FROM kaixhin/keras  
MAINTAINER Kai Arulkumaran <design@kaixhin.com>  
  
# Install nodejs  
RUN apt-get update && apt-get install -y vim curl lxc  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs build-essential  
  
# Clone FGMachine repo for RAM example  
RUN cd /root && git clone https://github.com/Leo-Gao/FGMachine.git && cd
FGMachine && \  
npm install  
  
# Install sk learn  
RUN pip install -U scikit-learn  
  
# For ssl key  
RUN export SSL_KEY=key.pem  
RUN export SSL_CERT=cert.pem  
RUN openssl req -x509 -newkey rsa:4096 -keyout $SSL_KEY -out $SSL_CERT -days 7
-nodes -subj '/CN=localhost'  
  
# Expose port  
EXPOSE 443  
EXPOSE 8080  
#EXPOSE 5081  
# Set working directory  
WORKDIR /root/FGMachine  
# Start server  
ENTRYPOINT ["node", "machine"]

