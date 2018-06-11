FROM google/nodejs  
  
LABEL maintainer.name="Anthony PERIQUET"  
LABEL maintainer.email="anthony@periquet.net"  
LABEL version="0.2.0"  
LABEL description="Terminal over HTTP and HTTPS"  
  
ARG SHELL  
ARG GROUP  
ARG USER  
ARG PASS  
  
ENV SHELL ${SHELL:-/bin/bash}  
ENV GROUP ${GROUP:-wetty}  
ENV USER ${USER:-wetty}  
ENV PASS ${PASS:-pleaseChangeMe}  
  
RUN apt update && \  
apt install -y git python openssh-client  
  
# Clone repository in /opt/wetty and install dependencies  
RUN git clone https://github.com/krishnasrinivas/wetty /opt/wetty && \  
cd /opt/wetty && \  
npm install  
  
# Create ssh user  
RUN addgroup ${GROUP} && \  
adduser --system --ingroup ${GROUP} \--home /home/${USER} \--shell ${SHELL}
\--disabled-password ${USER} && \  
echo "${USER}:${PASS}" | chpasswd  
  
WORKDIR /opt/wetty  
  
ENTRYPOINT ["node"]  
CMD ["app.js", "-p", "3000"]

