FROM evol262/nodejs:latest  
  
ENV container docker  
STOPSIGNAL SIGRTMIN+3  
EXPOSE 9090  
RUN dnf -y install cockpit  
RUN systemctl enable cockpit.socket  
RUN useradd -m -G wheel development  
RUN echo "development:ovirt" | chpasswd  
  
WORKDIR /home/development  
# Install cockpit and deps  
RUN git clone https://github.com/cockpit-project/cockpit.git && \  
chown -R development:development cockpit  
RUN dnf -y install yum-plugin-ovl && yum clean all  
RUN yum-builddep -y cockpit/tools/cockpit.spec  
  
WORKDIR /home/development/cockpit  
USER development  
RUN sed -ie -s '/phantomjs/d' package.json && \  
mkdir ./tmp && \  
TMPDIR=./tmp yarn install  
  
RUN webpack  
RUN mkdir -p ~/.local/share/cockpit && \  
ln -s $(pwd)/dist/* ~/.local/share/cockpit  
  
USER root  
CMD [ "/sbin/init" ]  

