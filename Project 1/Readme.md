Group Members
<br>&emsp;Raviteja Reddy Guntaka (rguntak1@asu.edu)
<br>&emsp;Sai Manoja Gadde (sgadde4@asu.edu)
<br>&emsp;Karthik Chadalavada (ckarthik@asu.edu)

Group Contributions

<br>&emsp;Raviteja Reddy Guntaka: 
<br>&emsp;&emsp;Implemented Auto scaling and tested the application
<br>&emsp;&emsp;Created RESPONSE queue listener which will receive message on response queue and generate final output for user
<br>&emsp;&emsp;Create a continuous polling mechanism to monitor Response Queue.
<br>&emsp;&emsp;Provide Response to the user request with image name and class name.
<br>&emsp;&emsp;Configured AWS components and services for Auto Scaling and validated end-to-end functionality.

<br>&emsp;Sai Manoja Gadde: 
<br>&emsp;&emsp;Created elastic IP required to expose the flask app to consume requests
<br>&emsp;&emsp;Researched on the application frameworks to use and implemented flask app for web-tier
<br>&emsp;&emsp;Created helper functions for S3 tasks, to upload and download files.
<br>&emsp;&emsp;Integrated all the components for end-to-end functionality.

<br>&emsp;Karthik Chadalavada: Implemented App Tier
<br>&emsp;&emsp;Created AMI for App tier with auto start python service for image classification.
<br>&emsp;&emsp;Consume Message From Request Queue.
<br>&emsp;&emsp;Download the image from Input S3 Bucket.
<br>&emsp;&emsp;Use the given Model to classify the image.
<br>&emsp;&emsp;Upload the txt file consisting of file name and class name to Output S3 Bucket.
<br>&emsp;&emsp;Publish the image name and class name to Response Queue.

<br>Credentials
<br>&emsp;emailId : guntaka.ravitejareddy@gmail.com
<br>&emsp;password : Aws:1004teja
<br>
<br>PEM Key
<br>cloud_computing.pem
<br>
<br>
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAk6IdDEJ8sFm8B3AHPKzwWwlJDPhHFGSr+cr+hR3kxZmaPSW2
zU9LVMH+p1gLMXK8TWORJanGyf6bMrJWrVjAKEl4XyQlm47J+18v01oqF995+Odn
FVrWFoPfRrfEk1iXqBBIqqAWHB4FeU1afNVUOWezu9XlOnchmmGEH0UuxZ5o0uFe
USlpCCr5AQrCPovgWcx2qxM4lBELZtyrLyJfxYcYzEGRF3jyJfp31CDz+xckzaDX
Ez32N1Pq0usshPsxyJytqSjRlmqvqbzsreUvBt7qA4yVdA/1Yy3b6QQ7yZ6vwlV9
ewnTBrbATsnBvx/wrVRETFuwWMiDZnn2QEnvMQIDAQABAoIBAAPTyRL/SkI8IU7E
Dbv588U4aWdnrFgQABFavNxwmPSydbguGR4bdyV8XgCynJ+sjMso0KN8UkX8TsOy
seKOkXS56t/0jPEKc5wLrK67AKpbxcq5HQgFsdUlmA06SGNVgaD+wxOBUPFrqdKq
ObVQxn0yfgtZkTbBzeI1svoojfzbg18wZ5G06k9v65v9B6PV6UH+tnT45MUavbmf
efCYwnp0EyLn2elniikXxR19EwQqW/Zt0cuGzkshsSa5H2GnC8iRUa2DCanUbyvw
rbQYpBMvkEAROOrn1hrWkV38dNWCD2LiDNQFCxo0o+CIQlVF4rvWBBsRTvu5H4qs
RlF/ga0CgYEAyzbdy3z2mSAdzSjd/WJ0peaeFBARYfu6mtS/h1qZtLeLY9R3ghM9
T9xN7XK5my6FwNWwLgbsHpSCWctWSEA1Pb5J1eco68GMzp19Y6yFHJ53mNPfY91a
vWwg1EY5mMUi1wZd4CC1OaMTTauPUqtOXL/518QMNDP6DXpRDbZdkP8CgYEAuftG
grCQ1PnyfpRstkOsYmS4fN7o3WA1d5kDvc+bVz8FQuiSoxfnUghKaybDCHPDPsiC
e1dEKGiCRJLqnG3+isaA6ba93/md/evgD0rai+Emdds57Z05XFPEONLiUfVumlzT
Cy+OvfdXMV5ZMTg/3066afVWjx/Rbyw5ooIdT88CgYEAhI6vs1M6kLwwdGmaFPUq
XiXHLBMnI6FPIjxxC1wAM7AezuoDYugl8HgmpSNXC3EXcqhxmjSNxYzeUrCfAdZQ
ZIxCIbP+L3s73HNDHceltPtxzFE4wS3dSP7Fk3KTk6HUjirrBY6QaJ6Fsv6cKTLx
lPLtiN+rjknxbOVDBgzVkAUCgYAOsPvD7SCzwj7WovDngPcIGr68Fnu8qRHwLaUv
BExYGwFWZLrYqVW7lC4Uws4bR9G/juVHyv/2VTMdKaHg04uM+NtMGwRqwfQqD8z2
SEp1TEbWfofX7liOo4tXlckNAl9HUFfXhV04Qmaf3r0a9z+Ma1KsdhXtXm0T5CF1
ZePc3wKBgFLlvpA0KkAgxAMT/2g8FJxp5XddKvEI6zJ/Frtqk8jkOa92yauzK8h2
P6/xn8c5asVBcDsE2e6xKYBDscM2qW65O50iiRUeuZGLkSOQRhXUCG3D1cTa3y5e
B/MsRe1rqcjp1QBs6HTJI2w0FNe4RDHKPM8Rs95FtKFAtZjzlokA
-----END RSA PRIVATE KEY-----
<br>
<br>Web tier’s URL : 34.194.131.161
<br>EIP Web tier : 34.194.131.161
<br>SQS Request queue name : RequestMessageQueue
<br>SQS Response queue name : ResponseMessageQueue
<br>S3 input bucket : cloud-p1-input-bucket
<br>S3 output bucket : cloud-p1-output-bucket