FROM opensuse:tumbleweed  
RUN zypper --no-gpg-checks --non-interactive refresh && \  
zypper --non-interactive install nginx && \  
zypper --non-interactive clean -a  
WORKDIR /mnt  
CMD ["nginx", "-g", "daemon off;"]  

