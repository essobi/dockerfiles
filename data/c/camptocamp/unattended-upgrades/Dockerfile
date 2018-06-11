FROM busybox  
  
CMD echo -e 'APT::Periodic::Update-Package-Lists
"1";\nAPT::Periodic::Unattended-Upgrade "1";' >
/target/etc/apt/apt.conf.d/20auto-upgrades  

