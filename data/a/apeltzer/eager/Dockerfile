# Archlinux base image including yaourt  
FROM finalduty/archlinux:daily  
  
# Update everything, install our local repository with EAGER packages  
RUN echo "Server = http://mirror.de.leaseweb.net/archlinux/\$repo/os/\$arch"
>> /etc/pacman.d/mirrorlist  
RUN echo "[lambdait]" >> /etc/pacman.conf  
RUN echo "SigLevel = Never" >> /etc/pacman.conf  
RUN echo "Server = https://lambda.informatik.uni-tuebingen.de/repo/mypkgs/" >>
/etc/pacman.conf  
RUN pacman -Syu --noconfirm  
RUN pacman -S --noconfirm freetype2 ttf-dejavu sudo git libcups mesa-libgl
rsync strace r python2 gsl libxtst  
  
#Install all the dependencies of my pipelin  
##Installing Required Packages  
##Oracle JDK7, BT2, BWA, Samtools, etc.  
#Install all the dependencies of my pipeline  
RUN pacman -S --noconfirm --force jdk bam2tdf dedup circularmapper
clipandmerge fastqc preseq vcf2genome fastx_toolkit htslib qualimap mapdamage
bwa eager-reportengine eagerstat  
RUN pacman -S --noconfirm --force bowtie2 picard-tools stampy angsd  
RUN pacman -S --noconfirm --force schmutzi eager-gui eager-cli gatk  
RUN mkdir -p /data  
RUN rm /var/cache/pacman/pkg/*  
  
# Add GATK Licence to image to be consistent with Licencing Permission by
Broad Institute  
ADD GATKLicence.txt /usr/share/licenses/common/GATKLicence.txt  
  
# X11 login  
RUN pacman -S --noconfirm openssh openssl  
RUN pacman -S --noconfirm xorg-xauth  
RUN pacman -S --noconfirm xorg-xhost  
RUN pacman -S --noconfirm xorg-xeyes  
RUN ssh-keygen -A  
RUN sed -i -e 's/#X11Forwarding.*/X11Forwarding yes/' /etc/ssh/sshd_config  
RUN sed -i -e 's/#UseLogin.*/UseLogin no/' /etc/ssh/sshd_config  
RUN sed -i -e 's/#AllowTcpForwarding.*/AllowTcpForwarding yes/'
/etc/ssh/sshd_config  
RUN sed -i -e 's/#X11UseLocalhost.*/X11UseLocalhost yes/' /etc/ssh/sshd_config  
RUN sed -i -e 's/#X11DisplayOffset.*/X11DisplayOffset 10/'
/etc/ssh/sshd_config  
RUN echo "eager ALL=(ALL) ALL" >> /etc/sudoers  
  
## Install supervisord  
RUN pacman -S supervisor --noconfirm  
RUN rm /var/cache/pacman/pkg/*  
RUN sed -i -e 's/nodaemon=.*/nodaemon=true/' /etc/supervisord.conf  
ADD etc/supervisor.d/sshd.ini /etc/supervisor.d/sshd.ini  
  
## ssh key  
RUN mkdir -p /home/eager/.ssh  
RUN touch /home/eager/.ssh/authorized_keys  
RUN chmod 600 /home/eager/.ssh/authorized_keys  
ADD ssh_eager_rsa.key.pub /tmp/  
RUN cat /tmp/ssh_eager_rsa.key.pub >> /home/eager/.ssh/authorized_keys;rm -f
/tmp/ssh_eager_rsa.key.pub  
  
## user  
RUN echo "root:root" |chpasswd  
ADD opt/qnib/bin/create-user.sh /opt/qnib/bin/  
ADD etc/supervisor.d/create-user.ini /etc/supervisor.d/  
  
EXPOSE 22  
CMD [ "supervisord", "-c", "/etc/supervisord.conf" ]  

