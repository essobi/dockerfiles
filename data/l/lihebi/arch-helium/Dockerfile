FROM lihebi/arch-server  
  
# clone helium  
# user  
RUN useradd -m user && echo "user:user" | chpasswd  
RUN echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && chmod 0440
/etc/sudoers.d/user  
  
USER user  
ENV USER_HOME /home/user  
WORKDIR $USER_HOME  
RUN git clone https://github.com/lihebi/helium  
WORKDIR helium  
RUN mkdir build  
WORKDIR build  
RUN cmake ..  
RUN make -j4  
  
WORKDIR ..  
RUN ./setup.sh  
RUN source $USER_HOME/.bashrc  
WORKDIR $USER_HOME  

