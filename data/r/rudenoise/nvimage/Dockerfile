FROM alpine:3.7  
  
RUN apk update && \  
apk upgrade && \  
apk add --update --no-cache \  
neovim \  
git \  
bash \  
curl \  
wget \  
bind-tools \  
tree \  
python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
COPY ./bash/* /root/  
  
WORKDIR /root  
  
RUN ./vim.bash  
  
  
#RUN ./vim.bash  

