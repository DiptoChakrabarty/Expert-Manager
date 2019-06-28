# Expert-Manager
Automated menu that provides face authentication to website and features to reduce human interface.

## Setup for menu

### Yum Should be configured

```
yum install httpd
systemctl start httpd
systemctl enable httpd
```

### copy files to Document root

```
cp -r expert_manager/www/cgi-bin /var/www
cp -r expert_manager/www/html /var/www
```

### Flask Should be installed

```
pip install Flask
```
### for cv2 module open-cv library should be installed

```
pip install opencv-python
```



### Run server

```
python expert_manager/expert/main.py
```

### Teach your face to database
```
http://0.0.0.0:5000/signup
```


### Open Browser with given link
```
http://0.0.0.0:5000
```

### Many more packages are required to perform this task i will update them soon ThankYou for visiting


