FROM nkzhaowj/base-puppeteer:1.0  
# html静态文件  
# EXPOSE 9200  
# EXPOSE 8088  
# # 挂载本地html存储位置  
VOLUME ["/mobile-lighthouse/lib/public/output"]  
# # 挂载用户配置  
VOLUME ["/mobile-lighthouse/src/config/coustom"]  
# VOLUME ["/elasticsearch-6.2.2/data"]  
# VOLUME ["/elasticsearch-6.2.2/logs"]  
VOLUME ["/root/logs"]  
VOLUME ["/etc/supervisor/log"]  
  
# ENTRYPOINT ["/mobile-lighthouse.sh"]  
# CMD ["bin/bash"]  
CMD ["/mobile-lighthouse.sh"]

