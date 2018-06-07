FROM ansibleapp/ansibleapp-base  
# MAINTAINER {{ $MAINTAINER }}  
LABEL "com.redhat.ansibleapp.version"="0.1.0"  
LABEL "com.redhat.ansibleapp.spec"=\  
"aWQ6IGYzMmRlM2JjLTMyMjUtNDI5YS1iMjNiLWNlZjQ3Y2ExZDI1YgpuYW1lOiBhbnNpYmxlYXBw\  
L2V0aGVycGFkLWFuc2libGVhcHAKZGVzY3JpcHRpb246IE5vdGUgdGFraW5nIHdlYiBhcHBsaWNh\  
dGlvbgpiaW5kYWJsZTogdHJ1ZQphc3luYzogIm9wdGlvbmFsIgpwYXJhbWV0ZXJzOgogIC0gbmFt\  
ZTogZGF0YWJhc2VfdXNlcgogICAgZGVzY3JpcHRpb246IERhdGFiYXNlIFVzZXIKICAgIGRlZmF1\  
bHQ6IGV0aGVycGFkCiAgLSBuYW1lOiBkYXRhYmFzZV9wYXNzd29yZAogICAgZGVzY3JpcHRpb246\  
IERhdGFiYXNlIFBhc3N3b3JkCiAgLSBuYW1lOiBkYXRhYmFzZV9uYW1lCiAgICBkZXNjcmlwdGlv\  
bjogRGF0YWJhc2UgTmFtZQogICAgZGVmYXVsdDogZXRoZXJwYWQKICAtIG5hbWU6IGRhdGFiYXNl\  
X2hvc3QKICAgIGRlc2NyaXB0aW9uOiBEYXRhYmFzZSBzZXJ2aWNlIGhvc3RuYW1lL2lwCiAgICBk\  
ZWZhdWx0OiBtYXJpYWRiCiAgLSBuYW1lOiByb290X3Bhc3N3b3JkCiAgICBkZXNjcmlwdGlvbjog\  
cm9vdCBwYXNzd29yZCBmb3IgbWFyaWFkYiBjb250YWluZXIKICAtIG5hbWU6IGFwcGxpY2F0aW9u\  
X3Bhc3N3b3JkCiAgICBkZXNjcmlwdGlvbjogUGFzc3dvcmQgZm9yIGV0aGVycGFkLWxpdGUgYWRt\  
aW4gaW50ZXJmYWNlCiAgLSBuYW1lOiBzZXNzaW9uX2tleQogICAgZGVzY3JpcHRpb246IEtleSBm\  
b3IgcmVjb3ZlcmluZyBzZXNzaW9uLiBXaWxsIGRlZmF1bHQgdG8gcmFuZG9tIFVVSUQKICAgIHJl\  
cXVpcmVkOiBmYWxzZQo="  
ADD ansible /opt/ansible  
ADD ansibleapp /opt/ansibleapp  
  
RUN useradd -u 1001 -r -g 0 -M -b /opt/ansibleapp -s /sbin/nologin -c
"ansibleapp user" ansibleapp  
RUN chown -R 1001:0 /opt/{ansible,ansibleapp}  
USER 1001  

