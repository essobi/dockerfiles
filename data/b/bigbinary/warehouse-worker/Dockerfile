FROM bigbinary/image-builder  
  
RUN sudo apt-get -qq -y install ttf-freefont otf-freefont  
RUN sudo -H -i -u ubuntu pip install Pillow  
  
USER ubuntu  
  
WORKDIR /home/ubuntu/warehouse-worker  
ADD ./ /home/ubuntu/warehouse-worker  
  
RUN sudo chown -R ubuntu:ubuntu /home/ubuntu/warehouse-worker  
  
RUN crontab cron-xvfb-running  
RUN chmod +x /home/ubuntu/warehouse-worker/xvfb-running.sh  
  
RUN echo '# start cron daemon' >> $HOME/.bashrc  
RUN echo 'sudo cron' >> $HOME/.bashrc  
  
RUN echo 'sudo umount /dev/shm' >> $HOME/.bashrc  
RUN echo 'sudo mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=256M
tmpfs /dev/shm' >> $HOME/.bashrc  
  
RUN /bin/bash -c 'source $HOME/.bashrc ; rvm use 2.3.1 --default; bin/setup'  
ENTRYPOINT /bin/bash -c 'source $HOME/.bashrc ; sudo rm -f /tmp/.X11-unix/X99
; sudo rm -f /tmp/.X99-lock ; sudo /etc/rc.local; rvm use 2.3.1 --default ;
./bin/shoryuken -r ./lib/warehouse_worker.rb -C config/shoryuken.yml'  

