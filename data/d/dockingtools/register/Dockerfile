FROM alpine  
  
ENV REGISTER_VERSION 0.0.10  
ADD https://github.com/docking-
tools/register/releases/download/0.0.10/register /register  
COPY example/config.json /root/.docking/config.json  
  
RUN chmod +x /register  
  
CMD ["/register"]

