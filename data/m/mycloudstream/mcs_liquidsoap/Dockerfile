FROM mycloudstream/mcs_liquidsoap:latest  
MAINTAINER contact@mycloudstream.net  
  
# My Cloud Stream : Update  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# My Cloud Stream : Install Dev  
RUN apt-get -y install nano  
RUN apt-get -y install wget  
RUN apt-get -y install htop  
RUN apt-get -y install sudo  
  
# My CLoud Stream : Install Service SSH  
RUN apt-get install -y openssh-server  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/StrictModes yes/#StrictModes yes/' /etc/ssh/sshd_config  
RUN sed -i 's/PrintMotd no/PrintMotd yes/' /etc/ssh/sshd_config  
RUN sed -i 's/PasswordAuthentication yes/#PasswordAuthentication no/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN mkdir -p /root/.ssh  
RUN echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABJQAAAQEAm1a44V+ZdIPPmpbFx9fqmANpCb5t/PU3sBUEvdAjEq6dthRZFUQnLCYc8LCllyGOWfjypjGGbG1iUam6+HtmMeUIG20vVMKUjgxWDSfesyakhdeLQnghLTkrg5Xf83kHkqA8YlgorsLqfpNMt+hbuFxZ2X6YeRiRyoOf+yhCibDQnYRJhkxj5/P6/3T6Ixn0mY4gmSUZ6c+tuR9nbpVTSlZxElnMeFjBWGb2N+xnwUfkfJK99hKD9TyqPS7QNvAen37M3kLdiqxgNwFI5BRzRzYBqAI4ITtFDS7VERj/hmHr7fDMnqELVDAKZzTcIbTMkD50mPPTNMeNE4SlMb+0sQ==
My Cloud Stream" >> /root/.ssh/authorized_keys  
  
# My CLoud Stream : Install services Liquidsoap  
RUN adduser --disabled-password --no-create-home --gecos '' mycloudstream  
RUN usermod -a -G root mycloudstream  
  
# My CLoud Stream : Install Liquidsoap Server  
RUN apt-get install -y liquidsoap  
  
# My CLoud Stream : Init  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

