docker build -t img_classifier .

# use the following line to create a container and connect to bash
# docker run -it -p 8080:8080 img_classifier /bin/bash
docker run -p 8080:8080 img_classifier