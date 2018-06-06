FROM evol262/nodejs:latest  
  
ENV container docker  
  
RUN useradd -m -G wheel development  
RUN echo "development:ovirt" | chpasswd  
  
WORKDIR /home/development  
USER development  
  
RUN mkdir -p ~/.local/share/cockpit  
  
RUN mkdir -p ~/sources/dist  
  
RUN ln -s /home/development/sources/dist \  
/home/development/.local/share/cockpit/hacking  
  
WORKDIR /home/development/sources  
CMD [ "/home/development/sources/build.sh" ]  

