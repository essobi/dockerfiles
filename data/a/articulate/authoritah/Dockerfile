FROM ubuntu  
MAINTAINER Luke van der Hoeven <plukevdh@articulate.com>  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
jq \  
libyaml-dev \  
libgc-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -s https://api.github.com/repos/articulate/authoritah/releases/latest
|\  
jq --raw-output '.assets | map(select(.name == "authoritah-linux"))[0] |
.browser_download_url' |\  
xargs curl -L -o authoritah -s  
RUN chmod +x authoritah  
  
RUN mkdir /auth0  
VOLUME /auth0  
WORKDIR /auth0  
  
ENTRYPOINT ["../authoritah"]  

