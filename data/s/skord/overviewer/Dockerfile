FROM phusion/passenger-full:0.9.15  
ADD default /etc/nginx/sites-available/default  
RUN apt-get update &&\  
apt-get install -y python-imaging python-numpy wget  
ADD 40_run_overviewer.sh /etc/my_init.d/40_run_overviewer.sh  
RUN rm -f /etc/service/nginx/down &&\  
mkdir /home/app/world_map &&\  
chown app:app /home/app/world_map &&\  
chmod +x /home/app/world_map &&\  
chmod +x /etc/my_init.d/40_run_overviewer.sh  
USER app  
ENV HOME /home/app  
RUN wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/1.8.jar -P
~/.minecraft/versions/1.8/  
USER root  
ENV HOME /root  
ADD http://overviewer.org/builds/1084/overviewer-0.12.22-deb64.deb
/tmp/overviewer-0.12.22-deb64.deb  
RUN dpkg -i /tmp/overviewer-0.12.22-deb64.deb  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["/sbin/my_init"]  

