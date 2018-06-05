FROM bizzotech/frappe-base:latest  
MAINTAINER Emad Shaaban <emad@bizzotech.com>  
  
# Update  
ENV FRAPPE_USER frappe  
ENV BENCH_BRANCH master  
ENV FRAPPE_BRANCH v10.0.0  
RUN groupadd -r $FRAPPE_USER && \  
useradd -r -m -g $FRAPPE_USER $FRAPPE_USER && \  
echo 'frappe ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers  
  
  
USER $FRAPPE_USER  
WORKDIR /home/$FRAPPE_USER  
RUN git clone -b $BENCH_BRANCH \--depth 1 https://github.com/BizzoTech/bench
bench-repo && \  
sudo pip install -e /home/$FRAPPE_USER/bench-repo --no-cache-dir && \  
mkdir -p frappe-bench && cd frappe-bench && \  
mkdir -p apps logs sites config && \  
bench setup env && \  
sudo bench setup sudoers $FRAPPE_USER && \  
bench setup socketio && \  
bench get-app frappe https://github.com/frappe/frappe --branch $FRAPPE_BRANCH
&& \  
cd /home/$FRAPPE_USER/frappe-bench/apps/frappe && npm install && \  
cd /home/$FRAPPE_USER/frappe-bench && npm install babel-preset-env && \  
rm -rf /home/$FRAPPE_USER/bench-repo/.git && \  
rm -rf /home/$FRAPPE_USER/frappe-bench/apps/frappe/.git  
  
ADD ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN sudo chmod +x /usr/local/bin/docker-entrypoint.sh  
  
VOLUME /home/$FRAPPE_USER/frappe-bench/logs  
  
WORKDIR /home/$FRAPPE_USER/frappe-bench  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["app"]  

